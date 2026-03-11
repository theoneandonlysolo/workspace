
#ifndef ASCII_REF_H
# define ASCII_REF_H

/* isascii — valid ASCII range */
# define ASCII_MIN          0
# define ASCII_MAX          127

/* isprint — visible/printable characters */
# define PRINT_MIN          32    /* space */
# define PRINT_MAX          126   /* ~ */

/* isdigit — '0' through '9' */
# define DIGIT_MIN          48    /* '0' */
# define DIGIT_MAX          57    /* '9' */

/* isupper / toupper — uppercase A–Z */
# define UPPER_MIN          65    /* 'A' */
# define UPPER_MAX          90    /* 'Z' */

/* islower / tolower — lowercase a–z */
# define LOWER_MIN          97    /* 'a' */
# define LOWER_MAX          122   /* 'z' */

/* toupper / tolower — distance between cases */
# define CASE_OFFSET        32    /* 'a' - 'A' == 32 */

/* isalpha covers UPPER_MIN–UPPER_MAX and LOWER_MIN–LOWER_MAX */
/* isalnum covers isalpha + isdigit                            */

/* Special named characters */
# define ASCII_NUL          0     /* '\0' — null terminator (strlen stops here) */
# define ASCII_TAB          9     /* '\t' */
# define ASCII_NEWLINE      10    /* '\n' */
# define ASCII_SPACE        32    /* ' '  */
# define ASCII_DEL          127   /* DEL  — last ASCII, not printable */

/* ─────────────────────────────────────────────
**  CLASSIFICATION MACROS
**  Each macro is a direct translation of its
**  C standard library counterpart.
** ───────────────────────────────────────────── */

/* isascii(c) — is c a valid ASCII value? */
# define IS_ASCII(c)   ((c) >= ASCII_MIN && (c) <= ASCII_MAX)

/* isprint(c) — is c visible when printed? (space counts) */
# define IS_PRINT(c)   ((c) >= PRINT_MIN && (c) <= PRINT_MAX)

/* isdigit(c) — is c a digit character '0'–'9'? */
# define IS_DIGIT(c)   ((c) >= DIGIT_MIN && (c) <= DIGIT_MAX)

/* isupper(c) — is c an uppercase letter? */
# define IS_UPPER(c)   ((c) >= UPPER_MIN && (c) <= UPPER_MAX)

/* islower(c) — is c a lowercase letter? */
# define IS_LOWER(c)   ((c) >= LOWER_MIN && (c) <= LOWER_MAX)

/* isalpha(c) — is c any letter, upper or lower? */
# define IS_ALPHA(c)   (IS_UPPER(c) || IS_LOWER(c))

/* isalnum(c) — is c a letter OR a digit? */
# define IS_ALNUM(c)   (IS_ALPHA(c) || IS_DIGIT(c))

/* toupper(c) — shift lowercase to uppercase, leave others untouched */
# define TO_UPPER(c)   (IS_LOWER(c) ? (c) - CASE_OFFSET : (c))

/* tolower(c) — shift uppercase to lowercase, leave others untouched */
# define TO_LOWER(c)   (IS_UPPER(c) ? (c) + CASE_OFFSET : (c))

/* ─────────────────────────────────────────────
**  FULL ASCII TABLE (comment reference)
**
**  DEC | HEX  | CHAR | NOTE
**  ────────────────────────────────────────────
**    0 | 0x00 | NUL  | null terminator
**    1 | 0x01 | SOH  | start of heading
**    2 | 0x02 | STX  | start of text
**    3 | 0x03 | ETX  | end of text
**    4 | 0x04 | EOT  | end of transmission
**    5 | 0x05 | ENQ  | enquiry
**    6 | 0x06 | ACK  | acknowledge
**    7 | 0x07 | BEL  | bell (audible alert)
**    8 | 0x08 | BS   | backspace
**    9 | 0x09 | HT   | horizontal tab
**   10 | 0x0A | LF   | line feed / newline
**   11 | 0x0B | VT   | vertical tab
**   12 | 0x0C | FF   | form feed
**   13 | 0x0D | CR   | carriage return
**   14 | 0x0E | SO   | shift out
**   15 | 0x0F | SI   | shift in
**   16 | 0x10 | DLE  | data link escape
**   17 | 0x11 | DC1  | device control 1
**   18 | 0x12 | DC2  | device control 2
**   19 | 0x13 | DC3  | device control 3
**   20 | 0x14 | DC4  | device control 4
**   21 | 0x15 | NAK  | negative acknowledge
**   22 | 0x16 | SYN  | synchronous idle
**   23 | 0x17 | ETB  | end of trans. block
**   24 | 0x18 | CAN  | cancel
**   25 | 0x19 | EM   | end of medium
**   26 | 0x1A | SUB  | substitute
**   27 | 0x1B | ESC  | escape
**   28 | 0x1C | FS   | file separator
**   29 | 0x1D | GS   | group separator
**   30 | 0x1E | RS   | record separator
**   31 | 0x1F | US   | unit separator
**   32 | 0x20 |  ' ' | SPACE — first printable
**   33 | 0x21 |  !   |
**   34 | 0x22 |  "   |
**   35 | 0x23 |  #   |
**   36 | 0x24 |  $   |
**   37 | 0x25 |  %   |
**   38 | 0x26 |  &   |
**   39 | 0x27 |  '   |
**   40 | 0x28 |  (   |
**   41 | 0x29 |  )   |
**   42 | 0x2A |  *   |
**   43 | 0x2B |  +   |
**   44 | 0x2C |  ,   |
**   45 | 0x2D |  -   |
**   46 | 0x2E |  .   |
**   47 | 0x2F |  /   |
**   48 | 0x30 |  0   | DIGIT_MIN
**   49 | 0x31 |  1   |
**   50 | 0x32 |  2   |
**   51 | 0x33 |  3   |
**   52 | 0x34 |  4   |
**   53 | 0x35 |  5   |
**   54 | 0x36 |  6   |
**   55 | 0x37 |  7   |
**   56 | 0x38 |  8   |
**   57 | 0x39 |  9   | DIGIT_MAX
**   58 | 0x3A |  :   |
**   59 | 0x3B |  ;   |
**   60 | 0x3C |  <   |
**   61 | 0x3D |  =   |
**   62 | 0x3E |  >   |
**   63 | 0x3F |  ?   |
**   64 | 0x40 |  @   |
**   65 | 0x41 |  A   | UPPER_MIN
**   66 | 0x42 |  B   |
**   67 | 0x43 |  C   |
**   68 | 0x44 |  D   |
**   69 | 0x45 |  E   |
**   70 | 0x46 |  F   |
**   71 | 0x47 |  G   |
**   72 | 0x48 |  H   |
**   73 | 0x49 |  I   |
**   74 | 0x4A |  J   |
**   75 | 0x4B |  K   |
**   76 | 0x4C |  L   |
**   77 | 0x4D |  M   |
**   78 | 0x4E |  N   |
**   79 | 0x4F |  O   |
**   80 | 0x50 |  P   |
**   81 | 0x51 |  Q   |
**   82 | 0x52 |  R   |
**   83 | 0x53 |  S   |
**   84 | 0x54 |  T   |
**   85 | 0x55 |  U   |
**   86 | 0x56 |  V   |
**   87 | 0x57 |  W   |
**   88 | 0x58 |  X   |
**   89 | 0x59 |  Y   |
**   90 | 0x5A |  Z   | UPPER_MAX
**   91 | 0x5B |  [   |
**   92 | 0x5C |  \   |
**   93 | 0x5D |  ]   |
**   94 | 0x5E |  ^   |
**   95 | 0x5F |  _   |
**   96 | 0x60 |  `   |
**   97 | 0x61 |  a   | LOWER_MIN
**   98 | 0x62 |  b   |
**   99 | 0x63 |  c   |
**  100 | 0x64 |  d   |
**  101 | 0x65 |  e   |
**  102 | 0x66 |  f   |
**  103 | 0x67 |  g   |
**  104 | 0x68 |  h   |
**  105 | 0x69 |  i   |
**  106 | 0x6A |  j   |
**  107 | 0x6B |  k   |
**  108 | 0x6C |  l   |
**  109 | 0x6D |  m   |
**  110 | 0x6E |  n   |
**  111 | 0x6F |  o   |
**  112 | 0x70 |  p   |
**  113 | 0x71 |  q   |
**  114 | 0x72 |  r   |
**  115 | 0x73 |  s   |
**  116 | 0x74 |  t   |
**  117 | 0x75 |  u   |
**  118 | 0x76 |  v   |
**  119 | 0x77 |  w   |
**  120 | 0x78 |  x   |
**  121 | 0x79 |  y   |
**  122 | 0x7A |  z   | LOWER_MAX
**  123 | 0x7B |  {   |
**  124 | 0x7C |  |   |
**  125 | 0x7D |  }   |
**  126 | 0x7E |  ~   | PRINT_MAX
**  127 | 0x7F | DEL  | not printable
** ───────────────────────────────────────────── */

#endif /* ASCII_REF_H */