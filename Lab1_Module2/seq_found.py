#!/usr/bin/python3
import sys


def id_extract(file):
	id={}
	fasta=open(file,"r")
	for line in fasta:
		line=line.rstrip()
		#print(line)
		if line[0]==">":
			if "|" in line:
				line=line.split("|")
				temp=">"+ line[1]
				id[temp]=""
			else:
				temp=line
				id[temp]=""
		else:
			id[temp]+=line
	return id


def new_file(db_id, file_id, operation,filename):
	res=open(filename+".fasta","w")
	for key in db_id:
		if operation=="2":
			if key not in file_id:
				if len(db_id[key]) > 60:
					split_seq=""
					for i in range(0,len(db_id[key]),60):
						temp=db_id[key][i:60+i] + "\n"
						split_seq= split_seq + temp
					fasta=key + "\n" + split_seq
					res.write(fasta)
				else:
					fasta=key + "\n" + db_id[key] + "\n"
					res.write(fasta)
		else:
			if key in file_id:
				if len(db_id[key]) > 60:
					split_seq=""
					for i in range(0,len(db_id[key]),60):
						temp=db_id[key][i:60+i] + "\n"
						split_seq= split_seq + temp
					fasta=key + "\n" + split_seq
					res.write(fasta)
				else:
					fasta=key + "\n" + db_id[key] + "\n"
					res.write(fasta)


if __name__ == "__main__":
	db=sys.argv[1]
	in_file=sys.argv[2]
	db_id=(id_extract(db))
	file_id=(id_extract(in_file))
	operation=input("1 to extract sequence from DB, 2 to remove: ")
	filename=input("Name of the otput: ")
	new_file(db_id,file_id,operation,filename)
