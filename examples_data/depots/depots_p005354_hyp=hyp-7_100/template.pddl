(define (problem depots-test)
(:domain depots)
(:objects
		depot0 - Depot
		distributor0 - Distributor
		truck0 - Truck
		truck1 - Truck
		pallet0 - Pallet
		pallet1 - Pallet
		crate0 - Crate
		crate1 - Crate
		crate2 - Crate
		crate3 - Crate
		crate4 - Crate
		crate5 - Crate
		crate6 - Crate
		crate7 - Crate
		hoist0 - Hoist
		hoist1 - Hoist
)
(:init

	(at crate3 depot0)
	(on crate3 crate2)
	(available hoist0)
	(clear crate6)
	(clear crate5)
	(on crate0 pallet1)
	(available hoist1)
	(at hoist1 depot0)
	(at crate6 distributor0)
	(at crate0 distributor0)
	(at crate4 distributor0)
	(at pallet1 distributor0)
	(on crate2 pallet0)
	(on crate6 crate1)
	(at crate5 depot0)
	(on crate5 crate3)
	(at truck0 depot0)
	(at crate1 distributor0)
	(at truck1 depot0)
	(at crate7 distributor0)
	(on crate1 crate4)
	(at hoist0 distributor0)
	(at crate2 depot0)
	(at pallet0 depot0)
	(on crate7 crate0)
	(on crate4 crate7)
)
(:goal 
(and
<HYPOTHESIS>
))
)