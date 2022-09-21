import glob
import sys
import os

from pydub import AudioSegment
dirpath = "c/" #This sets the directory
start = dirpath+"Users/" #This contains the first wav file
second = dirpath+"/include/" #this contains three wav files
final = "merged.wav"

filenames = glob.glob(start+'*.wav')
aud1  = AudioSegment.from_wav(second + "aud1.wav")
aud2 = AudioSegment.from_wav(includeDir + "aud2.wav")
aud3     = AudioSegment.from_wav(includeDir + "aud3.wav")

newfile= [aud1,aud3]
combined = AudioSegment.empty()
for i in filenames:
	afname = AudioSegment.from_wav(i)
	newfile.extend([afname, aud3])
  
newfile.extend([aud2])
for i in newfile:
    combined += i

combined.export(start + final, format="wav")
