#include "KStream.h"

/**
* Opaque KStream Data Structure Pointer 
*/
typedef struct kstream_s* KStream;

/**
* Unsinged byte data type for easier code readability
*/
typedef unsigned char byte;

struct kstream_s {
    byte* key;
    size_t keylen;
    byte* S;
    int i;
    int j;
}

byte next_byte(KStream kstream) {
    kstream->i = (kstream->i + 1) % 256;
    kstream->j = (kstream->j = kstream->S[kstream->i]) % 256;
    byte si2 = kstream->S[i];
    byte sj2 = kstream->S[j];
    kstream->S[i] = sj2;
    kstream->S[j] = si2;
    return kstream->S[(kstream->S[kstream->i] + kstream->S[kstream->j]) % 256]
}

KStream ks_create(byte* key, size_t keylen) {
    KStream kstream = (KStream)malloc(sizeof(struct kstream_s));
    kstream->key = (byte*)malloc(sizeof(byte) * keylen);
    kstream->S = (byte*)malloc(sizeof(byte) * 256);

    for (int i = 0; i < 256; i++) {
        kstream->S[i] = i;
    }

    int j = 0;
    for (int i = 0; i < 256; i++) {
        j = (j + kstream->S[i] + key[i % keylen]) % 256;
        byte si2 = kstream->S[i];
        byte sj2 = kstream->S[j];
        kstream->S[i] = sj2;
        kstream->S[j] = si2;
    }

    kstream->j = j;
    kstream->i = 255;

    for (int i = 0; i < 1024; i++) {
        next_byte(kstream);
    }
}

byte ks_translate(KStream kstream, byte data_byte) {
    return data_byte ^ next_byte(kstream);
}

void ks_destroy(KStream kstream) {
    free(kstream->key);
    free(kstream->S);
    free(kstream);
}
