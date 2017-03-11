var Pong = function(){
		var canvas = document.getElementById('myCanvas');
		canvas.style.left = 50;
		canvas.width = window.innerWidth-100;
		canvas.height = window.innerHeight-100;
		var context = canvas.getContext('2d');
		var scoreBoard = document.getElementById('scoreBoard');
		var margin = canvas.width/10;
		var world = Physics();
		var score = {bot:0 , player:0};
		var renderer = Physics.renderer('canvas', {
		    el: 'myCanvas', // id of the canvas element
		    autoResize:false,
		    height:canvas.height,
		    width:canvas.width
		});
		var ball , playerHandle ,botHandle;
		document.getElementById('msgBoard').innerHTML = "";
		world.add( renderer );
		world.add(Physics.behavior('interactive', { el: renderer.container }));
		world.add(Physics.behavior("body-impulse-response"));
  				// enabling collision detection among bodies
  		world.add(Physics.behavior("body-collision-detection"));
		world.add(Physics.behavior("sweep-prune"));
		
		world.add(Physics.behavior("edge-collision-detection", {
      	     		aabb: Physics.aabb(0, 0, canvas.width, canvas.height),
	      			restitution: 0.6
  				}));

		
		var handleDimensions = {radius:canvas.width/50};
		
		var initialPositions = {
			ball:{
				x:canvas.width/2,
				y:canvas.height/2 
			},
			playerHandle:{
				x:canvas.width-handleDimensions.radius-margin,
				y:canvas.height/2 
			},
			botHandle:{
				x:margin+handleDimensions.radius,
				y:canvas.height/2 
			}
		}
		
  			ball = Physics.body('circle' , 
			{	x:canvas.width/2,
				y:canvas.height/2 ,
				radius:handleDimensions.radius/2,
				restitution:0.9 , 
				cof:0.8,
				mass:100,
				styles:
					{
						strokeStyle: 'white',
						lineWidth: 5,
						fillStyle: '#FF6600',
						angleIndicator: '#FF6600'
					},
				label:'puck'	
			});

			botHandle = Physics.body('circle' , 
			{	x:margin+handleDimensions.radius,
				y:canvas.height/2 , 
				radius:handleDimensions.radius,
				treatment:'static',
				mass:100,
				styles:
					{  	
						strokeStyle: 'white',
						lineWidth: 5,
						fillStyle: '#8B668B',
						angleIndicator: '#8B668B'
					}
			});

			playerHandle = Physics.body('circle' , 
			{	x:canvas.width-handleDimensions.radius-margin,
				y:canvas.height/2 , 
				radius:handleDimensions.radius,
				treatment:'static',
				styles:
					{
						strokeStyle: 'white',
						lineWidth: 5,
						fillStyle: '#8B668B',
						angleIndicator: '#8B668B'
					}
			});
  		

		var botGoal = Physics.body('rectangle',
		{
			x:0,
			y:canvas.height/2,
			width:margin/4,
			height:handleDimensions.radius*6,
			treatment:'static',
			label:'botGoal',
			styles:
			{
				strokeStyle: 'white',
				fillStyle:'white',
				angleIndicator:'#EEDD82'
			}

		});

		var playerGoal = Physics.body('rectangle',
		{
			x:canvas.width,
			y:canvas.height/2,
			width:margin/4,
			height:handleDimensions.radius*6,
			treatment:'static',
			label:'playerGoal',
			styles:
			{
				strokeStyle: 'white',
				fillStyle:'white',
				angleIndicator:'#EEDD82'
			}
		});
		world.add(ball);
		world.add(botHandle);
		world.add(playerHandle);
		world.add(botGoal);
		world.add(playerGoal);
		var botai = new Bot(botHandle,playerHandle , ball , world);

		var playerGoalPuckCollisionQuery = Physics.query({
		    $or: [
		        { bodyA: { label: 'puck' }, bodyB: { label: 'playerGoal' } }
		        ,{ bodyB: { label: 'puck' }, bodyA: { label: 'playerGoal' } }
		    ]
		});

		var botGoalPuckCollisionQuery = Physics.query({
		    $or: [
		        { bodyA: { label: 'puck' }, bodyB: { label: 'botGoal' } }
		        ,{ bodyB: { label: 'puck' }, bodyA: { label: 'botGoal' } }
		    ]
		});
		

		world.on('collisions:detected', function( data, e ){
		    // find the first collision that matches the query
		    var founda = Physics.util.find( data.collisions, playerGoalPuckCollisionQuery);
		    if ( founda )
		    	score.bot += 1;
		    var foundb = Physics.util.find( data.collisions, botGoalPuckCollisionQuery);
		    if ( foundb )
		    	score.player += 1;
		   botScore.innerHTML = "BOT: " + score.bot ;
		   playerScore.innerHTML =  score.player + " :PLAYER";  
		    if(founda || foundb){
		    	msgBoard.innerHTML = "GOAL!!!";
		    	//canvas.style.visibility = "hidden";
		    	
		    	world.pause();
		    	    count = 4;
		    	    startTime = Date.now();
			    	interval = setInterval(function(){
			    			var msg = document.getElementById('msgBoard');
			    			count -= 1
			    			msg.innerHTML = count;

			    			if(Date.now() - startTime >  1600)
			    			{
			    			    document.getElementById('msgBoard').innerHTML = "";
			    			    window.clearInterval(interval);
			    			    resetBodies();
			    			    world.unpause();
			    			}
			    	} ,500)		    	
		    	
		    }
		    
		});
		world.render();

  		world.on("step",function(){
    					world.render();
    					drawField();
    					botai.update();
				});

  		renderer.addLayer("Field");
  
  		drawField = function(){
  			renderer.drawLine(
  					{x:canvas.width/4 , y:canvas.height/4},
  					{x:canvas.width/4 , y:canvas.height*3/4}, 
  					{
						strokeStyle: '#ffffff',
						lineWidth: 5,
						fillStyle: '#0099CC',
						angleIndicator: '#0099CC'
					}, 
					context);

  			renderer.drawLine(
  					{x:canvas.width*3/4 , y:canvas.height/4},
  					{x:canvas.width*3/4 , y:canvas.height*3/4}, 
  					{
						strokeStyle:'#ffffff',
						lineWidth: 5,
						fillStyle: '#0099CC',
						angleIndicator: '#0099CC'
					}, 
					context);

  			renderer.drawLine(
  					{x:0, y:0},
  					{x:0 , y:canvas.height}, 
  					{
						strokeStyle: '#A62A2A',
						lineWidth: 5,
						fillStyle: '#0099CC',
						angleIndicator: '#0099CC'
					}, 
					context);

  			renderer.drawLine(
  					{x:canvas.width , y:0},
  					{x:canvas.width , y:canvas.height}, 
  					{
						strokeStyle: '#A62A2A',
						lineWidth: 5,
						fillStyle: '#0099CC',
						angleIndicator: '#0099CC'
					}, 
					context);
  		}

  		resetBodies = function(){
  			var bodies = {a:ball , b:playerHandle , c:botHandle};
  			ball.state.pos.set(initialPositions.ball.x , initialPositions.ball.y);
  			playerHandle.state.pos.set(initialPositions.playerHandle.x , initialPositions.playerHandle.y);
  			botHandle.state.pos.set(initialPositions.botHandle.x , initialPositions.botHandle.y);
		   	for(var prop in bodies){
		    	resetBodyPhysics(bodies[prop]);
		    }
  		}
  		resetBodyPhysics = function(body){
  			body.state.vel.set(0,0);
  			body.state.acc.set(0,0);
  			body.state.angular.pos = 0;
			body.state.angular.vel  = 0;
			body.state.angular.acc = 0;
			body.recalc();
  		}
  		Physics.util.ticker.on(function(time,dt){
    					world.step(time);
  				});
		Physics.util.ticker.start()	
};

window.setTimeout(function () {
    Pong();

} , 5000)