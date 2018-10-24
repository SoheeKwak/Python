import numpy as np

trees = np.loadtxt('data/trees.csv', delimiter=',',skiprows=1, unpack=True) # skiprows=1 1행을 건너뛴다(문자열은 numpy(수치화)하지못해서 에러나므로
print(trees.shape) #31행 3열 =>unpack=True 3행 31열로 변환
print(trees[:-1]) #3열(volume)은 읽지 말고,1,2열(girth, height)만 출력
print("="*50)
print(trees[[-1]]) #마지막 열, 즉, 3열(volume)만 출력