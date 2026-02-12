(define (problem driverlog-test)
(:domain driverlog)
(:objects
		driver1 - driver
		driver2 - driver
		driver3 - driver
		truck1 - truck
		truck2 - truck
		package1 - obj
		package2 - obj
		package3 - obj
		package4 - obj
		package5 - obj
		s0 - location
		s1 - location
		s2 - location
		p2-0 - location
		p7-1 - location
)
(:init
	(link s0 s1)
	(path p2-0 s1)
	(at package1 s0)
	(path s0 p7-1)
	(at package4 s1)
	(path s0 p2-0)
	(path p7-1 s0)
	(empty truck1)
	(path p2-0 s0)
	(empty truck2)
	(at driver1 s2)
	(at driver2 s0)
	(at package3 s2)
	(link s0 s2)
	(path s1 p2-0)
	(path s2 p7-1)
	(at truck1 s2)
	(at package5 s1)
	(path p7-1 s2)
	(at package2 s1)
	(at truck2 s0)
	(at driver3 s0)
	(link s2 s0)
	(link s1 s0)
)
(:goal 
(and
<HYPOTHESIS>
))
)