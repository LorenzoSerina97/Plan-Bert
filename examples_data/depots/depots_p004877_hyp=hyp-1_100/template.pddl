(define (problem depots-test)
(:domain depots)
(:objects
		depot0 - Depot
		depot1 - Depot
		distributor0 - Distributor
		distributor1 - Distributor
		truck0 - Truck
		truck1 - Truck
		pallet0 - Pallet
		pallet1 - Pallet
		pallet2 - Pallet
		pallet3 - Pallet
		crate0 - Crate
		crate1 - Crate
		hoist0 - Hoist
		hoist1 - Hoist
		hoist2 - Hoist
		hoist3 - Hoist
)
(:init

	(clear pallet3)
	(at hoist2 depot1)
	(at truck0 depot1)
	(clear crate0)
	(available hoist0)
	(clear crate1)
	(on crate0 pallet1)
	(available hoist1)
	(available hoist2)
	(at pallet2 depot0)
	(at pallet0 distributor0)
	(available hoist3)
	(at crate1 depot0)
	(at hoist3 distributor1)
	(at hoist1 depot0)
	(on crate1 pallet2)
	(clear pallet0)
	(at truck1 depot0)
	(at hoist0 distributor0)
	(at pallet1 depot1)
	(at pallet3 distributor1)
	(at crate0 depot1)
)
(:goal 
(and
<HYPOTHESIS>
))
)