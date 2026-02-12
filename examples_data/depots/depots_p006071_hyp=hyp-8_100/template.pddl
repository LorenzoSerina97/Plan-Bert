(define (problem depots-test)
(:domain depots)
(:objects
		depot0 - Depot
		depot1 - Depot
		depot2 - Depot
		distributor0 - Distributor
		distributor1 - Distributor
		distributor2 - Distributor
		truck0 - Truck
		truck1 - Truck
		truck2 - Truck
		pallet0 - Pallet
		pallet1 - Pallet
		pallet2 - Pallet
		pallet3 - Pallet
		pallet4 - Pallet
		pallet5 - Pallet
		crate0 - Crate
		crate1 - Crate
		crate2 - Crate
		hoist0 - Hoist
		hoist1 - Hoist
		hoist2 - Hoist
		hoist3 - Hoist
		hoist4 - Hoist
		hoist5 - Hoist
)
(:init

	(on crate1 pallet3)
	(at pallet5 depot0)
	(at hoist2 depot1)
	(clear pallet2)
	(clear crate0)
	(on crate0 crate1)
	(available hoist0)
	(at pallet0 distributor1)
	(available hoist1)
	(at hoist5 distributor0)
	(available hoist2)
	(at crate2 distributor1)
	(at pallet3 depot1)
	(at truck2 distributor0)
	(available hoist3)
	(at hoist3 distributor1)
	(at hoist1 depot0)
	(available hoist4)
	(at pallet2 depot2)
	(at hoist0 distributor2)
	(at pallet1 distributor0)
	(clear pallet5)
	(at hoist4 depot2)
	(on crate2 pallet0)
	(at truck1 distributor1)
	(clear crate2)
	(at pallet4 distributor2)
	(at truck0 distributor1)
	(clear pallet4)
	(available hoist5)
	(clear pallet1)
	(at crate1 depot1)
	(at crate0 depot1)
)
(:goal 
(and
<HYPOTHESIS>
))
)