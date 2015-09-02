var myapp = angular.module("myApp",[]);

myapp.controller("myController",function($scope){	
//	   $(".myDropdownHandle").dropdown('toggle');
	 $scope.desig = "Designation";   
	
		   $('#demolist li a').on('click', function(){
			    alert($(this).text());
  
			    $scope.desig = $(this).text();
			    
			    $scope.dropdown1 = $(this).text();
			    $scope.$apply();
			});

		   
		  
		   
	
});