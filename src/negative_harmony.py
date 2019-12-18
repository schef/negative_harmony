#!/usr/bin/env python

from music21 import *

print("use # for sharp and - for flat")
keyString = input("insert major key: ")
chromaticScale = scale.ChromaticScale(keyString).getPitches()
upperNotes = [chromaticScale[10], chromaticScale[11], chromaticScale[0], chromaticScale[1], chromaticScale[2], chromaticScale[3]]
lowerNotes = [chromaticScale[9], chromaticScale[8], chromaticScale[7], chromaticScale[6], chromaticScale[5], chromaticScale[4]]

while(True):
    chordString = input("insert chord: ")
    # chordString = "g b d f"
    positiveChord = chord.Chord(chordString.split())
    print("positiveChord:", chord.Chord(positiveChord).pitchedCommonName)

    negativeChord = []

    for note in positiveChord.notes:
        #search in upper
        for i,n in enumerate(upperNotes):
            if note.pitch.pitchClass == n.pitchClass:
                print("adding", note.pitch, "->", lowerNotes[i])
                negativeChord.append(lowerNotes[i])
        #search in lower
        for i,n in enumerate(lowerNotes):
            if note.pitch.pitchClass == n.pitchClass:
                print("adding", note.pitch, "->", upperNotes[i])
                negativeChord.append(upperNotes[i])

    print("negativeChord:", chord.Chord(negativeChord).pitchedCommonName)