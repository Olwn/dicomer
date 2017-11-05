# dicomer

## install

```shell
git clone https://github.com/pydicom/pydicom.git --depth=1
cd pydicom && python setup.py install
```

## usage
Assuming files are organized as following

* a_directory/  
     * patient1/  
        * 1.dcm  
        * 2.dcm  
     * patient2/  
        * 1.dcm
     * ...

```shell
 git clone https://github.com/Olwn/dicomer.git
 cd dicomer
 python main.py path/to/a_directory
```
For each patient, the program will generate one new directory 
containing same number of DICOM files. The 'PatientName' and 'PatientBirthDate' are removed.
