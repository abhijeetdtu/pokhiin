app.directive('sequencer',["$timeout"  ,'soundService' , function ($timeout , soundService) {
    return {
        restrict: 'E',
        scope: {
            key: '=',
            height: '=',
            width: '=',
            notes: '@',
            tempos:'='
        },
        // template: function (element, attrs) { return '<div id="' + attrs.key + '"><button ng-click="fillRandomNotes()">Randomize</button></div>' },
        template: function (element, attrs) { console.log("returning template"); return '<div ng-include="\'Views/Partials/Sequencer.html\'" onload="init()" ></div>' },
        link: function (scope, element, attrs, ctrl) {
            console.log("linking", element);
            scope.key = attrs.key;
            scope.rows = attrs.row
            scope.cols = attrs.col
            
            scope.getRows = function () {
                var rr = [];
                for (var i = 0 ; i < scope.rows ; i++)
                    rr.push(i);
                return rr;
            }
            
            scope.synths = [
                "sine","square","sawtooth","triangle"
            ]
            scope.selections = {};
            for (var i = 0 ; i < scope.rows ; i++)
                scope.selections[i] = scope.synths[Math.floor(scope.synths.length*Math.random())];
            scope.selectInstrument = function (rowId, instrumentId) {
                scope.selections[rowId] = scope.synths[instrumentId];
            }
            
            scope.noteNames = attrs.notes.split(",");
            scope.tempo = "16n";
            scope.tempos = JSON.parse(attrs.tempos);
            scope.setTempo = function (tempo) {
                scope.tempo = tempo;
                Tone.Transport.clear(scope.loopId);
                scope.startLoop();
                scope.$apply();
            }
            //Wait for load of template
            scope.init = function () {
                
                //Wait for application of scope to the dom
                $timeout(function () {

                    //Wait for Nx to load
                    soundService.OnNxLoad(function (obj) {
                        id = attrs.key + "Canvas";
                        nx.add("matrix", { name: id, parent: attrs.key, h: attrs.height, w: attrs.width })
                   
                        scope.widget = nx.widgets[id]
                        scope.widget.row = attrs.row
                        scope.widget.col = attrs.col
                        scope.widget.init();

                        scope.widget.on("*", function () {
                            scope.filled = false;
                            for (var i = 0; i < scope.widget.col ; i++)
                                for (var j = 0 ; j < scope.widget.row ; j++)
                                    if (scope.widget.matrix[i][j] === 1) {
                                        scope.filled = true;
                                        scope.$apply();
                                        break;
                                    }
                        })
                       
                        scope.synth = new Tone.MonoSynth().toMaster();;
                        //
                        //scope.noteNames = ['E5', 'D4', 'B4', 'A4', 'G4', 'E4'];
                        scope.stepNumber = 0;

                        console.log(Tone.Transport)

                        scope.fillRandomNotes= function() {
                            for (var i = 0; i < scope.widget.col; i++) {
                                for (var j = 0; j < scope.widget.row; j++) {
                                    if (Math.random() < .2) {
                                        scope.widget.matrix[i][j] = 1;
                                    }
                                    else {
                                        scope.widget.matrix[i][j] = 0;
                                    }
                                  
                                }
                            }
                            scope.widget.draw()
                            scope.filled = true;
                        }
                        
                        scope.clear = function () {
                            for (var i = 0; i < scope.widget.col; i++) 
                                for (var j = 0; j < scope.widget.row; j++)       
                                    scope.widget.matrix[i][j] = 0;

                            scope.filled = false;
                            scope.widget.draw();
                             
                        }


                        scope.fillRandomNotes();

                        //var chord = new Tone.Event(function (time, chord) {
                        //    //the chord as well as the exact time of the event
                        //    //are passed in as arguments to the callback function
                        //}, ["D4", "E4", "F4"]);
                        ////start the chord at the beginning of the transport timeline
                        //chord.start();
                        ////loop it every measure for 8 measures
                        //chord.loop = 8;
                        //chord.loopEnd = "1m";
                        scope.startLoop = function () {
                            scope.loopId = Tone.Transport.scheduleRepeat(function (time) {
                                var column = scope.widget.matrix[scope.stepNumber];
                                var rows = scope.widget.row;
                                for (var i = 0; i < rows; i++) {
                                    if (column[i] === 1) {

                                        //console.log(scope.noteNames[i % scope.noteNames.length])
                                        //scope.synths[scope.selections[i]].triggerAttackRelease(scope.noteNames[i % scope.noteNames.length], "32n", time);
                                        scope.synth.oscillator.type = scope.selections[i];
                                        scope.synth.triggerAttackRelease(scope.noteNames[i % scope.noteNames.length], "32n", time);
                                    }
                                }
                                scope.stepNumber++;
                                scope.stepNumber = scope.stepNumber % scope.widget.col;
                            }, scope.tempo)
                            
                        }
                       
                        //var loop = new Tone.Sequence(function (time) {
                    
                        //}, "16n");
                        Tone.Transport.loopEnd = "1m";
                        Tone.Transport.loop = true;
                        Tone.Transport.start();
                        scope.startLoop();
                        //loop.start();
                    });
                } , 2000);
                
            
            }

        }
    }
}]);