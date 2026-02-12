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

	(on crate2 crate6)
	(at crate3 depot0)
	(clear crate0)
	(available hoist0)
	(on crate6 crate3)
	(on crate0 crate4)
	(available hoist1)
	(at crate1 depot0)
	(at truck1 distributor0)
	(at truck0 distributor0)
	(at crate0 distributor0)
	(at crate4 distributor0)
	(at pallet1 distributor0)
	(on crate1 pallet0)
	(at crate6 depot0)
	(at hoist0 depot0)
	(at hoist1 distributor0)
	(at crate7 distributor0)
	(on crate7 crate5)
	(clear crate2)
	(at crate2 depot0)
	(at pallet0 depot0)
	(on crate3 crate1)
	(on crate5 pallet1)
	(on crate4 crate7)
	(at crate5 distributor0)
)
(:goal 
(and
<HYPOTHESIS>
))
)