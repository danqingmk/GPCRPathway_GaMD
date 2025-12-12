
export CUDA_VISIBLE_DEVICES=0

pmemd.cuda -O -i min.in -o min.out -p com.prmtop -c com.inpcrd -r min.rst -ref com.inpcrd

pmemd.cuda -O -i heat.in -o heat.out -p com.prmtop -c min.rst -r heat.rst -x heat.nc -ref min.rst

pmemd.cuda -O -i equil1.in -o equil1.out -p com.prmtop -c heat.rst -r equil1.rst -x equil1.nc -ref heat.rst

pmemd.cuda -O -i equil2.in -o equil2.out -p com.prmtop -c equil1.rst -r equil2.rst -x equil2.nc -ref equil1.rst










