import numpy as np
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '2'

Work_Dic='/data/home/guest/spike/sumd_7'
seed = 40
Num = 1 
X = [1,2,3,4,5,6,7,8]
Ini = 100

command_1 = 'pmemd.cuda -O -i SuMD.in -o SuMD_1.out -p com.prmtop -c SuMD_0.rst -r SuMD_1.rst -x SuMD_1.nc\nmv gamd.log gamd1.log'
os.system(command_1)

while seed >= 5:
  Y=[]
  cpp_file = 'trajin SuMD_' + str(Num) + '.nc 1 -1 10\nreference com.inpcrd [first] \n rms rms1 ref [first] :1-597&!@H= out rms.dat \nreference ref.inpcrd [last] \nrms rms2 ref [last] :703-771@C,CA,N,O out distance_' + str(Num) + '.out nofit\n'
  open('distance.in', 'w').write(cpp_file)
  cpp_command = 'cpptraj -p com.prmtop -i distance.in'
  os.system(cpp_command)
  fo = open('distance_' + str(Num) + '.out', 'r')
  for line in fo.readlines():
    if '#' not in line:
      dis = str(line).split()[-1].replace('\n', '')
      Y.append(float(dis))
  seed = min(Y)
  Z = np.polyfit(X,Y,1)
  m = Z[0]
  if Y[7] < Y[0]  and m < 0:
    command = 'pmemd.cuda -O -i SuMD.in -o SuMD_' + str(Num+1) + '.out -p com.prmtop -c SuMD_' + str(Num) + '.rst -r SuMD_' + str(Num+1) + '.rst -x SuMD_' + str(Num+1) + '.nc\nmv gamd.log gamd_' +  str(Num+1) + '.log'
    Num+=1
    Ini = Y[7]
    os.system(command)
  else:
    command = 'pmemd.cuda -O -i SuMD.in -o SuMD_' + str(Num) + '.out -p com.prmtop -c SuMD_' + str(Num-1) + '.rst -r SuMD_' + str(Num) + '.rst -x SuMD_' + str(Num) + '.nc\nmv gamd.log gamd_' +  str(Num) + '.log'
    os.system(command)

os.system('cp SuMD_' + str(Num) + '.rst prod0.rst')
os.system('sh ' + Work_Dic + 'CMD.sh')
						

