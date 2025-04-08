#!/usr/bin/env python

def read_fastq():
    fastq_list = []
    with open("lab9.fq", 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 4):
            header = lines[i].strip()
            sequence = lines[i + 1].strip()
            plus = lines[i + 2].strip()
            quality = lines[i + 3].strip()
            fastq_list.append((header, sequence, plus, quality))
    return fastq_list

def quality_to_scores(quality_str):
    return [ord(char) - 33 for char in quality_str] #convert ASCII to numerical


def sliding_window_trim(header, sequence, plus, quality):
    scores = quality_to_scores(quality)
    window_size = 10
    threshold = 15

    remove_indices = []
    for i in range(len(scores) - window_size + 1):
        window_avg = sum(scores[i:i + window_size]) / window_size #getting average
        if window_avg < threshold:
            for j in range(i, i + window_size):
                remove_indices.append(j)

    trimmed_seq = ''.join(sequence[i] for i in range(len(sequence)) if i not in remove_indices)
    trimmed_qual = ''.join(quality[i] for i in range(len(quality)) if i not in remove_indices)

    return header, trimmed_seq, plus, trimmed_qual


def process_fastq():
    fastq_list = read_fastq()
    for header, sequence, plus, quality in fastq_list:
        trimmed_header, trimmed_seq, trimmed_plus, trimmed_qual = sliding_window_trim(header, sequence, plus, quality)
        print(trimmed_header)
        print(trimmed_seq)
        print(trimmed_plus)
        print(trimmed_qual)
process_fastq()