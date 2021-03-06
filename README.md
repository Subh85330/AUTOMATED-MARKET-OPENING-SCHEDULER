# AUTOMATED-MARKET-OPENING-SCHEDULER
Implementation of the paper "Segregation of Heterogeneous Units in a Swarm of Robotic Agents" Authors-Manish Kumar; Devendra P. Garg; Vijay Kumar

In the problem, we have been given 'n' types of shops and 'm' market places which can be opened parallely. In a market place during
each time slot the 'k' types of shops can be opened. and for each market there are a total of 'T' time slots available.

Used local search strategy to solve this problem and followed the following desirable attributes for a good schedule
1. All types of shops opening in one time slot in the same market should sell related item.
2. All types of shops opening in parallel markets should be as far away as possible to avoid people’s movement to all of the markets.


Scearch Strategy Procedure:
PART-1) First of all, considered the problem in terms of markets only and ignore the time-slots
	- randomly chosen one shop and put this first shops in the first market place.
	- For arranging the first market, added shops which have maximum similarity from the shops currently in the session. 
	  where similarity value for a shop have been calculated as:- 
 				similarity(i,j) =  (1 - distance(i,j).
	- For second market, added the shops which are at maximum distance from the shops of the first market and have maximum
          similarity value with shops in the second(current) market.
	- Similarly for the third market, added the shops which are at maximum distance from both first and second market and
          have maximum similarity from the shops of the third market.
	Repeated the same procedure if there are any more remaining markets.


PART-2) For arranging the shops in the given number of time slots T, sorted the shops in a market place and then divided the 
	shops into T time slots and divided shops into equal numbers of each market into T time slots.
 
