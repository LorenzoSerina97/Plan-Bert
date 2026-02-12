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

	(at pallet0 depot1)
	(clear pallet3)
	(clear crate0)
	(clear crate1)
	(available hoist0)
	(available hoist1)
	(at hoist0 depot1)
	(at pallet2 depot0)
	(available hoist2)
	(at crate2 distributor1)
	(at crate0 depot0)
	(at truck2 distributor0)
	(at pallet4 distributor0)
	(available hoist3)
	(at truck0 distributor2)
	(at truck1 distributor0)
	(at pallet5 depot2)
	(at pallet3 distributor2)
	(at hoist3 distributor1)
	(on crate1 pallet4)
	(at hoist2 distributor2)
	(available hoist4)
	(clear pallet5)
	(at pallet1 distributor1)
	(at hoist4 depot2)
	(at hoist1 distributor0)
	(at crate1 distributor0)
	(clear pallet0)
	(clear crate2)
	(at hoist5 depot0)
	(on crate0 pallet2)
	(available hoist5)
	(on crate2 pallet1)
)
(:goal 
(and
<HYPOTHESIS>
))
)