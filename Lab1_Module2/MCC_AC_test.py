#!/usr/bin/python3

import sys
import math


def get_data(file):
	e_val={}
	file=open(file,"r")
	for line in file:
		line=line.split()
		e_val[line[0]]=float(line[1])
	return e_val


def conf_mat(pos_eval,neg_eval,th):
	mat=[[0,0],[0,0]]
	id=[["",""],["",""]]
	for key in pos_eval:
		if pos_eval[key]<th:
			mat[0][0]+=1
		else:
			mat[1][0]+=1
			id[1][0]+=key + ","
	for key in neg_eval:
		if neg_eval[key]<th:
			mat[0][1]+=1
			id[0][1]+=key + ","
		else:
			mat[1][1]+=1
	return mat, id


def stats(mat):
	t_pos = mat[0][0]
	t_neg = mat[1][1]
	f_pos = mat[0][1]
	f_neg = mat[1][0]
	acc=(t_pos+t_neg)/(t_pos+t_neg+f_pos+f_neg)
	mcc=((t_pos*t_neg)-(f_pos*f_neg))/math.sqrt(max((t_pos+f_pos)*(t_pos+f_neg)*(t_neg+f_pos)*(t_neg+f_neg),1))
	return acc, mcc


if __name__=="__main__":
	positive=sys.argv[1]
	negative=sys.argv[2]
	pos_eval=get_data(positive)
	neg_eval=get_data(negative)
	for i in range(21):
		th=10**-i
		mat=conf_mat(pos_eval,neg_eval,th)
		mcc=(stats(mat[0]))
		print(th,"\t",mcc, mat[0])
		#if mat[1][0][1].count(",")<5 and mat[1][1][0].count(",")<5:
		#	print("False positive: ", mat[1][0][1])
		#	print("False negative ", mat[1][1][0])
