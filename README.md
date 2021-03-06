# Installation
Install PRISM, Syft (including MONA) and python3:

```sudo apt install python3 mona```

In your prefered directory:
```git clone git@github.com:prismmodelchecker/prism.git```

And:
```git clone git@github.com:saffiepig/Syft.git```

# Running the example
To run the example:

```cd gridworld_example```

Change script to use your copy of Syft's ltlf2fol tool. E.g., change line 2 of ./hoa_mona_ltlf2dfa_for_prism to:
```~/Development/reactive_synthesis/build/bin/ltlf2fol "$1" NNF > spec.mona```


Run prism with the external automaton tool:
```prism gridLTLf.nm ltlf.props -ltl2datool ./hoa_mona_ltlf2dfa_for_prism -ltl2dasyntax spot```



# If you need just part of the pipeline

To convert LTLf to First-Order Logic:
```syft ltlf2fol spec.ltlf NNF > spec.mona```

To build an automaton using mona:
```mona -w -u spec.mona```

# GandALF Experiments
Experiments for our GandALF 2020 submission can be found [here](https://github.com/andrewmw94/gandalf_2020_experiments).

# Older Instructions

The original pipeline:
Create spec.
Convert to automaton using syft+mona.
Call prism to see what variable names are used in the automaton.
Change our automaton to use these names.
Call prism with tool that feeds in our automaton.

LTL pipeline:
Create MDP and Spec.
Translate spec to equivalent LTL formula. Using ```ltlfilt --from-ltlf```
Modify MDP by adding transition to terminal state from each state.
Run prism on modified MDP and translated spec.


