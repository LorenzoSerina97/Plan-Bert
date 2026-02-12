(define (problem driverlog-test)
(:domain driverlog)
(:objects
		driver1 - driver
		driver2 - driver
		truck1 - truck
		truck2 - truck
		package1 - obj
		package2 - obj
		s0 - location
		s1 - location
		s2 - location
		p10-0 - location
		p11-10 - location
		p0-2 - location
		p1-4 - location
)
(:init
	(link s0 s1)
	(path s1 p0-2)
	(path s2 p10-0)
	(path p1-4 s0)
	(link s2 s1)
	(path p0-2 s0)
	(empty truck1)
	(path s0 p0-2)
	(path p10-0 s1)
	(empty truck2)
	(at driver2 s0)
	(link s0 s2)
	(at driver1 s0)
	(path p10-0 s2)
	(at truck1 s0)
	(path p0-2 s1)
	(path p1-4 s2)
	(at truck2 s0)
	(at package1 s1)
	(path s1 p10-0)
	(link s1 s2)
	(path s0 p1-4)
	(at package2 s2)
	(link s2 s0)
	(path s2 p1-4)
	(link s1 s0)
)
(:goal 
(and
<HYPOTHESIS>
))
)