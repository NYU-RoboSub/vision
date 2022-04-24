# /bin/bash
files_to_delete=`ls | grep -E 'CONTRAST|BLUR|MIRROR'`
echo $files_to_delete

for file in $files_to_delete
do
    rm $file
done
