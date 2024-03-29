#Retrieve the protein sequence of human insulin from human preproinsulin
#Access NCBI at https://ncbi.nlm.nih.gov.
#Next to the search bar, choose the dropdown menu and select Protein.
# Next, in the search bar, enter human insulin and choose Search-insulin(homo sapiens).
# now copy and paste the origin and // statement and add into file  preproinsulin-seq.txt:
#Obtaining the protein sequence of human insulin
#creating 4 sequences of amino acid i.e 
#1 In lsinsulin-seq-clean.txt, save amino acids 1–2
#2 In binsulin-seq-clean.txt, save amino acids 25–54.
#3 In cinsulin-seq-clean.txt, save amino acids 55–89
#4 In ainsulin-seq-clean.txt, save amino acids 90–110.
input_file = "preproinsulin-seq-clean.txt"
output_file = "lsinsulin-seq-clean.txt"


with open(input_file, "r") as f:
    text = f.read()

print("\n", text, "\n")

insuline_list = list(text)
#print(insuline_list)

lsinsulin = insuline_list[:24]
#print(lsinsulin)
#print(len(lsinsulin))

lsinsuline_seq_clean = "".join(lsinsulin)
# print(lsinsuline_seq_clean)

print("The first {} amino acids are:".format(len(lsinsulin)), lsinsuline_seq_clean)

mes = lsinsuline_seq_clean

with open(output_file, "w") as f:
    f.write(mes)


# ----------------amino acids 25–54------------------------------------------------

in_file = "preproinsulin-seq-clean.txt"
out_file = "binsulin-seq-clean.txt"

with open(in_file, "r") as f:
    text = f.read()


binsulin = insuline_list[24:54]
# print(binsulin)
print("This is a sequence of", len(binsulin), "characters.")

binsuline_seq_clean = "".join(binsulin)

print("The next {} amino acids are:".format(len(binsulin)), binsuline_seq_clean)

message = binsuline_seq_clean

with open(out_file, "w") as f:
    f.write(message)




# ----------------amino acids 55–89------------------------------------------------

in_file = "preproinsulin-seq-clean.txt"
out_file = "cinsulin-seq-clean.txt"

with open(in_file, "r") as f:
    text = f.read()


cinsulin = insuline_list[54:89]
# print(ainsulin)
print("This is a sequence of", len(cinsulin), "characters.")

cinsuline_seq_clean = "".join(cinsulin)

print("The next {} amino acids are:".format(len(cinsulin)), cinsuline_seq_clean)

message = cinsuline_seq_clean

with open(out_file, "w") as f:
    f.write(message)



# ----------------amino acids 90–110------------------------------------------------

in_file = "preproinsulin-seq-clean.txt"
out_file = "ainsulin-seq-clean.txt"

with open(in_file, "r") as f:
    text = f.read()


ainsulin = insuline_list[89:]
# print(ainsulin)
print("This is a sequence of", len(ainsulin), "characters.")

ainsuline_seq_clean = "".join(ainsulin)

print("The last {} amino acids are:".format(len(ainsulin)), ainsuline_seq_clean)

message = ainsuline_seq_clean

with open(out_file, "w") as f:
    f.write(message)