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


num_rows = 10
num_cols = 10

probN = 0.69
probE = 0.1
probW = 0.1
probB = 0.01
probS = 0.1

def rc2i(row, col):
    if row < num_rows and row >= 0 and col < num_cols and col >= 0:
        return row * num_rows + col
    return -1

def printNorth(row, col):
    extraProb = 0
    str = "[] x={} -> ".format(rc2i(i,j))
    if(rc2i(i-1, j) == -1):
        extraProb += probN
    else:
        str = str + " {}:(x'={}) +".format(probN, rc2i(i-1, j))
    if(rc2i(i+1, j) == -1):
        extraProb = extraProb + probB
    else:
        str = str + " {}:(x'={}) +".format(probB, rc2i(i+1, j))
    if(rc2i(i, j+1) == -1):
        extraProb = extraProb + probE
    else:
        str = str + " {}:(x'={}) +".format(probE, rc2i(i, j+1))
    if(rc2i(i, j-1) == -1):
        extraProb = extraProb + probW
    else:    
        str = str + " {}:(x'={}) +".format(probW, rc2i(i, j-1))
    print(str + " {}:(x'={});".format(probS+extraProb, rc2i(i,j)))

def printSouth(row, col):
    extraProb = 0
    str = "[] x={} -> ".format(rc2i(i,j))
    if(rc2i(i-1, j) == -1):
        extraProb += probB
    else:
        str = str + " {}:(x'={}) +".format(probB, rc2i(i-1, j))
    if(rc2i(i+1, j) == -1):
        extraProb = extraProb + probN
    else:
        str = str + " {}:(x'={}) +".format(probN, rc2i(i+1, j))
    if(rc2i(i, j+1) == -1):
        extraProb = extraProb + probW
    else:
        str = str + " {}:(x'={}) +".format(probW, rc2i(i, j+1))
    if(rc2i(i, j-1) == -1):
        extraProb = extraProb + probE
    else:    
        str = str + " {}:(x'={}) +".format(probE, rc2i(i, j-1))
    print(str + " {}:(x'={});".format(probS+extraProb, rc2i(i,j)))

def printEast(row, col):
    extraProb = 0
    str = "[] x={} -> ".format(rc2i(i,j))
    if(rc2i(i-1, j) == -1):
        extraProb += probW
    else:
        str = str + " {}:(x'={}) +".format(probW, rc2i(i-1, j))
    if(rc2i(i+1, j) == -1):
        extraProb = extraProb + probE
    else:
        str = str + " {}:(x'={}) +".format(probE, rc2i(i+1, j))
    if(rc2i(i, j+1) == -1):
        extraProb = extraProb + probN
    else:
        str = str + " {}:(x'={}) +".format(probN, rc2i(i, j+1))
    if(rc2i(i, j-1) == -1):
        extraProb = extraProb + probB
    else:    
        str = str + " {}:(x'={}) +".format(probB, rc2i(i, j-1))
    print(str + " {}:(x'={});".format(probS+extraProb, rc2i(i,j)))

def printWest(row, col):
    extraProb = 0
    str = "[] x={} -> ".format(rc2i(i,j))
    if(rc2i(i-1, j) == -1):
        extraProb += probE
    else:
        str = str + " {}:(x'={}) +".format(probE, rc2i(i-1, j))
    if(rc2i(i+1, j) == -1):
        extraProb = extraProb + probW
    else:
        str = str + " {}:(x'={}) +".format(probW, rc2i(i+1, j))
    if(rc2i(i, j+1) == -1):
        extraProb = extraProb + probB
    else:
        str = str + " {}:(x'={}) +".format(probB, rc2i(i, j+1))
    if(rc2i(i, j-1) == -1):
        extraProb = extraProb + probN
    else:    
        str = str + " {}:(x'={}) +".format(probN, rc2i(i, j-1))
    print(str + " {}:(x'={});".format(probS+extraProb, rc2i(i,j)))


print("mdp")
print("")
print("module M1")
print("")
print("    x : [0..{}] init 0;".format(num_rows*num_cols))

#print inner cells
for i in range (num_rows):
    for j in range (num_cols):
        printNorth(i,j)
        printSouth(i,j)
        printEast(i,j)
        printWest(i,j)

print("")
for i in range (num_rows*num_cols):
    print("[] x={} -> 1:(x'={});".format(i, num_rows*num_cols))
print("[] x={} -> 1:(x'={});".format(num_rows*num_cols, num_rows*num_cols))

print("")
print("endmodule")

print("")
print("// labels")
print("label \"initial\" = (x=0);")
print("label \"loca\" = (x=2);")
print("label \"locb\" = (x=4);")
print("label \"locc\" = (x=6);")
print("label \"locd\" =  (x=8);")
print("label \"locaa\" = (x=12);")
print("label \"locab\" = (x=14);")
print("label \"locac\" = (x=16);")
print("label \"locad\" =  (x=18);")
print("label \"bad\" = (x=5);")
print("label \"done\" = (x={});".format(num_rows*num_cols))