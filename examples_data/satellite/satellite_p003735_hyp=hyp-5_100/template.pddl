(define (problem satellite-test)
(:domain satellite)
(:objects
		satellite0
		instrument0
		instrument1
		image2
		infrared0
		infrared1
		GroundStation1
		GroundStation2
		Phenomenon5
		Phenomenon6
		Planet3
		Planet4
		Star0
		Star7
)
(:init
	(satellite satellite0)
	(instrument instrument0)
	(instrument instrument1)
	(mode image2)
	(mode infrared0)
	(mode infrared1)
	(direction GroundStation1)
	(direction GroundStation2)
	(direction Phenomenon5)
	(direction Phenomenon6)
	(direction Planet3)
	(direction Planet4)
	(direction Star0)
	(direction Star7)
	(calibration_target instrument0 Phenomenon6)
	(calibration_target instrument1 Star7)
	(supports instrument0 image2)
	(supports instrument0 infrared1)
	(supports instrument1 infrared0)
	(supports instrument1 infrared0)
	(supports instrument1 infrared1)
	(power_avail satellite0)
	(on_board instrument1 satellite0)
	(on_board instrument0 satellite0)
	(pointing satellite0 Star7)
)
(:goal 
(and
<HYPOTHESIS>
))
)