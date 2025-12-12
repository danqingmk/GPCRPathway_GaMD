export CUDA_VISIBLE_DEVICES=0

pmemd.cuda -O -i gamd_st.in  -o gamd_st.out -p com.prmtop -c equil2.rst -r gamd_st.rst -x gamd_st.nc -amd 

mv gamd.log gamd_st.log
