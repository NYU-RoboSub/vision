# /bin/bash
files_to_delete=`ls | grep -E 'xml'`
echo $files_to_delete

for file in $files_to_delete
do
    rm $file
done
