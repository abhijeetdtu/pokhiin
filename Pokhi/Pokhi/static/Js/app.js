
var app = angular.module('Pokhi', ['ui.router']);

    app.config(function ($stateProvider) {
        $stateProvider
        .state('home', {
            url : '/',
            templateUrl: '/Views/Home.html',
            controller: 'HomeController'
        })
        .state('base', {
            url: '/base',
            templateUrl: '/Views/Base.html',
            controller: 'BaseController'
        })
    });

    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    });

