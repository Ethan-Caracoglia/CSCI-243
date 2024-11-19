#include <stdio.h>
#include "KStream.h"
#include <string.h>

/**
* Opaque KStream Data Structure Pointer 
*/
typedef struct kstream_s* KStream;

/**
* Unsinged byte data type for easier code readability
*/
typedef unsigned char byte;

int main(int argc, char** argv) {
    byte key[8];
    byte buf;
    FILE* file;

    // Open and check the file for errors
    file = fopen(argv[1], "r");
    if (file == NULL) {
        printf("The key file could not be opened.");
        return 1;
    }

    // Read the key from the file and translate it to a 8 element byte array
    for (int i = 0; i < 8; i++) {
        fread(key[i], sizeof(byte), 1, file);
    }

    // Make sure to close the key file when I am finished.
    fclose(file);

    KStream kstream = ks_create(key, 8);

    file = fopen(argv[2], "r");
    if (file == NULL) {
        printf("The input file could not be opened.");
        return 1;
    }

    while (fread(&buf, sizeof(byte), 1, file) != 0) {
        if (strcmp(argv[2], "-") != 0) {
            
        }
    }
}