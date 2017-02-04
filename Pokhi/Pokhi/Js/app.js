
var app = angular.module('Pokhi', ['ui.router']);

app.config(function ($stateProvider) {
    $stateProvider
    .state('home', {
        url : '/',
        templateUrl: 'Home.html',
        controller: 'HomeController'
    })
});


