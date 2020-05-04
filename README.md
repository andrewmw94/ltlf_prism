Install PRISM, Syft (including MONA) and python3

To run the example:

cd gridworld_example

Change script to use your copy of Syft's ltlf2fol tool. E.g., change line 3 of ./hoa_mona_ltlf2dfa_for_prism to:
~/Development/reactive_synthesis/build/bin/ltlf2fol "$1" NNF > spec.mona


Run prism with the external automaton tool:
prism gridLTLf.nm ltlf.props -ltl2datool ./hoa_mona_ltlf2dfa_for_prism -ltl2dasyntax spot





To convert LTLf to First-Order Logic:
syft ltlf2fol spec.ltlf NNF > spec.mona

To build an automaton using mona:
mona -w -u spec.mona

The original pipeline:
Create spec.
Convert to automaton using syft+mona.
Call prism to see what variable names are used in the automaton.
Change our automaton to use these names.
Call prism with tool that feeds in our automaton.

The new pipeline:
Change script to use your copy of Syft's ltlf2fol tool
Create spec.
Call prism with our tool:
prism gridLTLf.nm ltlf.props -ltl2datool ./hoa_mona_ltlf2dfa_for_prism -ltl2dasyntax spot



LTL pipeline:
Create MDP and Spec.
Translate spec to equivalent LTL formula.
Modify MDP by adding transition to terminal state from each state.
Run prism on modified MDP and translated spec.


