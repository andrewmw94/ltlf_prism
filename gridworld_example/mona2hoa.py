# Copyright 2020 Andrew M. Wells
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import itertools

def convertMONAStringToHOA(str):
    out_str = ""
    for i in range(len(str)):
        if str[i] == "1":
            out_str = out_str + "{}& ".format(i)
        elif str[i] == "0":
            out_str = out_str + "!{}& ".format(i)
        elif str[i] == "X":
            out_str = out_str
        elif str[i] == " ":
            pass
        else:
            print("Error")

    return out_str[:-2]

def assgnToStr(bitList):
    out_str = ""
    for i in range(len(bitList)):
        if bitList[i] == 1:
            out_str = out_str + "{}& ".format(i)
        elif bitList[i] == 0:
            out_str = out_str + "!{}& ".format(i)
    return out_str[:-2]

def getAssgnDest(state_index, assgn, t_start, t_label, t_dest):
    ass = assgn
    for i in range(len(t_start)):
        if(t_start[i] == state_index):
            for j in range(len(ass)):
                if(ass[j] == 1 and t_label[i][j] == "0"):
                    break
                elif(ass[j] == 0 and t_label[i][j] == "1"):
                    break
                if(j == len(ass)-1):
                    return t_dest[i]

def convertMONAStateTransitionsToHOA(state_index, t_start, t_label, t_dest, num_AP, final_index, num_states):
    lst = list(itertools.product([0, 1], repeat=num_AP))
    if(state_index == final_index):
        for assgn in lst:
            print("[ {} ] {}".format(assgnToStr(assgn), final_index))
    else:
        for assgn in lst:
            print("[ {} ] {}".format(assgnToStr(assgn), getAssgnDest(state_index, assgn, t_start, t_label, t_dest)))

f=open(sys.argv[1], "r")
flines=f.readlines()

num_states = -1
num_AP = -1
AP_string = ""
start_state = -1
final_state = -1

transition_start = [] #ints
transition_label = [] #strings
transition_dest = [] #ints

for l in flines:
    if(l.startswith("State ")):
        transition_start.append(int(l[5:l.find(":")]))
        transition_label.append(l[l.find(": ")+2: l.find("->")-1])
        transition_dest.append(int(l[l.find("-> state")+8:-1]))
    elif(l.startswith("DFA for formula with free variables: ")):
        AP_string = l[37:-1] # remove the newline
        num_AP = len(AP_string.split())
    elif(l.startswith("Automaton has ")):
        num_states = int(l[13: 14+l[14:].find(" ")])
    elif(l.startswith("Initial state: ")):
        start_state = int(l[14:])
    elif(l.startswith("Accepting states: ")):
        final_state = int(l[17:])
    else:
        pass

strings = ["\"{}\" ".format(x.replace("P", "p")) for x in AP_string.split()] # Mona capitalized 'p'
s = ""
AP_string = s.join(strings)

print("HOA: v1")
print("States: {}".format(num_states))
print("AP: {} {}".format(num_AP, AP_string))
print("Start: {}".format(start_state))
print("acc-name: Buchi")
print("Acceptance: 1 Inf(0)")
print("properties: trans-labels explicit-labels state-acc no-univ-branch deterministic")
print("--BODY--")
j = 0
for i in range(num_states):
    if(i == final_state):
        print("State: {}".format(i) + " { 0 } ")
    else:
        print("State: {}".format(i))

    convertMONAStateTransitionsToHOA(i, transition_start, transition_label, transition_dest, num_AP, final_state, num_states)

print("--END--")
