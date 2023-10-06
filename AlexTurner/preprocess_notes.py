def replace_time(text, ori):
    """
    Replace times with divided up tokens representing the hour.
    E.g., 8:20 AM is replaced by t_forenoon
    Replace 2-digit redacted information that precedes time identifier with
    a generic token
    E.g., [**84**] AM is replaced by t_hour
    """
    r = ori
    if '**' in text:
        r = 'xxhour'
    else:
        try:
        # handle exceptions with custom rules
            f, s = text.split()
            s = 'am' if s[0] == 'a' else 'pm'
            l, r = f.split(':')
            if l == '' or l == '00':
                if r == '':
                    r = str(0).zfill(2)
                l = str(12)
            if int(l) > 12:
                l = str(int(l) % 12)
            f = ':'.join([l, r])
            text = ' '.join([f, s])

            d = datetime.strptime(text, '%I:%M %p')
            if d.hour >= 0 and d.hour < 4:
                r = 'xxmidngt'
            elif d.hour >= 4 and d.hour < 8:
                r = 'xxdawn'
            elif d.hour >= 8 and d.hour < 12:
                r = 'xxfore'
            elif d.hour >= 12 and d.hour < 16:
                r = 'xxafter'
            elif d.hour >=16 and d.hour <20:
                r = 'xxdusk'
            else:
                r = 'xxngt'
        except ValueError:
            pass
    return r

def replace_misc(text):
    """
    Replaces certain obvious easy to process items in the notes for helping
    downstream modeling
    """    
    # replace different types of "year old" with 
    # matches: y.o., y/o, years old. year old, yearold
    text = re.sub(r'-?\byears? ?-?old\b|\by(?:o|r)*[ ./-]*o(?:ld)?\b', ' yo', text, flags=re.IGNORECASE)

    # Does the same thing as above but copied from https://arxiv.org/abs/1808.02622v1
    text = re.sub(r'(\d+)\s*(year\s*old|y.\s*o.|yo|year\s*old|year-old|-year-old|-year old)', r'\1 yo', text, flags=re.IGNORECASE)
    
    # replaces yr, yr's, yrs with years
    text = re.sub(r'\byr[\'s]*\b', 'years', text, re.IGNORECASE)
    
    # replace Pt and pt with patient, and IN/OUT/OT PT with patient
    # Note: PT also refers to physical therapy and physical therapist
    text = re.sub(r'\b[P|p]t.?|\b(IN|OU?T) PT\b', 'patient ', text)

    # replace sex with consistant token
    text = re.sub(r'\b(gentlman|male|man|m|M)(?!\S)\b', 'male', text)
    text = re.sub(r'\b(female|woman|f|F)(?!\S)\b', 'female', text)
    
    # replace time types
    text = re.sub(r'\d{0,2}:\d{0,2} \b[A|P]\.?M\.?\b', replace_time, text, flags=re.IGNORECASE)
    text = re.sub(r'\[\*\*(\d{2})\*\*\] \b[a|p].?m.?\b', replace_time, text, flags=re.IGNORECASE)
    
    # finally remove leftover redacted stuff (mostly empty)
    text = re.sub(r'\[\*\*(.*?)\*\*\]', '', text, flags=re.IGNORECASE)

    return text