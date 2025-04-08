#!/usr/bin/env python

def gcContent(seq, sig_figs = 2):
    length = len(seq)
    g_count = seq.count('G')
    c_count = seq.count('C')
    gc_content = (g_count + c_count) / length
    return round(gc_content, sig_figs)

