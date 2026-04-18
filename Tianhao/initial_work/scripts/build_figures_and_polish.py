from pathlib import Path
import math
import re

import fitz
from PIL import Image, ImageDraw, ImageFont


BASE = Path(__file__).resolve().parents[1]
PDF_PATH = BASE / 'inputs' / 'FMRI_course.pdf'
OUT_DIR = BASE / 'outputs'
FIG_DIR = OUT_DIR / 'figures'
FIG_DIR.mkdir(parents=True, exist_ok=True)
FULL_MD = OUT_DIR / 'practical_fmri_textbook_full_manuscript.md'
POLISHED_MD = OUT_DIR / 'practical_fmri_textbook_full_manuscript_polished.md'
MANIFEST = OUT_DIR / 'figure_manifest.md'
TEXT_EXTRACTS = OUT_DIR / 'figure_text_extracts.md'

# num, caption, pages, columns
FIGS = [
    ('1.1', 'Net magnetization and signal strength dependence on magnetic field strength, B0.', [2, 3], 2),
    ('2.1', 'Rotating-frame view before excitation and the RF pulse.', [4, 5], 2),
    ('2.2', 'RF-pulse duration and flip-angle setting.', [6], 1),
    ('2.3', 'Magnetization after excitation and early dephasing.', [7, 8], 2),
    ('2.4', 'Signal detection and the NMR signal.', [9, 10], 2),
    ('3.1', 'The spin echo overview.', [11], 1),
    ('3.2', 'Spin-echo excitation and first evolution.', [12, 13], 2),
    ('3.3', 'Spin-echo refocusing and after-refocusing stages.', [14, 15], 2),
    ('3.4', 'Spin echo after second evolution.', [16], 1),
    ('3.5', 'Longitudinal relaxation time (T1).', [17], 1),
    ('3.6', 'Molecular origins of relaxation and the concept of spin temperature in relaxation.', [18, 19], 2),
    ('3.7', 'Diffusion, T2 and T2*.', [21], 1),
    ('3.8', 'Chemical shift.', [22], 1),
    ('4.1', 'Main MRI components.', [25], 1),
    ('4.2', 'Gradient coil.', [27], 1),
    ('4.3', 'Receive coil arrays and 32-channel coil.', [28, 29], 2),
    ('4.4', 'Receive field heterogeneity.', [30], 1),
    ('5.1', 'Conjugate-variable relationships between time and frequency, and between space and k-space.', [32, 33], 2),
    ('5.2', 'Complex-wave decomposition into component frequencies under the Fourier transform.', [34], 1),
    ('5.3', 'Fourier decomposition example showing component-frequency peaks for a complex signal.', [35], 1),
    ('5.4', 'Fourier transform notation, Euler relation, and example frequency spectra from time-varying signals.', [36], 1),
    ('5.5', 'Time-domain and frequency-domain illustration of Fourier decomposition for a complex signal.', [37], 1),
    ('5.6', 'Useful Fourier pairs that recur in MRI intuition.', [38], 1),
    ('5.7', 'One-dimensional gradient encoding and how position maps to frequency components.', [39, 40, 41, 42], 2),
    ('5.8', 'Historical projection imaging and Lauterbur’s early MRI logic.', [43], 1),
    ('6.1', 'Sinc-shaped RF pulse and rectangular excitation bandwidth, showing frequency-selective slice selection under Gz.', [44, 45, 46, 47], 2),
    ('6.2', 'Slice-selection gradient plus refocusing lobe.', [48], 1),
    ('6.3', 'Three-stage gradient-echo formation sequence.', [49, 50, 51, 52, 53], 3),
    ('7.1', 'Image space versus k-space, showing that they are Fourier pairs rather than different anatomical spaces.', [54, 55, 56], 3),
    ('7.2', 'Gradient-echo trajectory through kx and phase-encoding shifts through ky.', [61, 62, 63, 64, 65, 66, 67, 68], 4),
    ('7.3', 'Building a 2D k-space matrix line by line.', [69, 74, 75, 76, 77], 3),
    ('7.4', 'Effects of preserving only low or high spatial frequencies; reduced resolution and edge-enhanced images.', [78, 80, 81], 3),
    ('7.5', 'Aliasing and truncation artifact examples.', [83, 84], 2),
    ('8.1', 'Zig-zag EPI k-space trajectory with alternating read gradients and phase-encoding blips.', [87, 116], 2),
    ('8.2', 'Real EPI pulse sequence with slice select, echo train, and correction components.', [114, 115, 116], 3),
    ('8.3', 'Example of good EPI and corresponding temporal-SNR / standard-deviation images.', [117, 118], 2),
    ('9.1', 'Nyquist ghosting mechanism: odd/even line mismatch, zig-zag k-space, and half-FOV ghost formation.', [89, 90, 91, 92], 2),
    ('9.2', 'Time-varying ghosting shown with standard-deviation imagery.', [93, 94, 95], 3),
    ('9.3', 'Fat suppression on/off and chemical-shift contamination in EPI.', [97, 98, 99], 3),
    ('9.4', 'Distortion and bandwidth comparison between read and phase directions.', [102, 103, 104, 105, 106], 3),
    ('9.5', 'Signal dropout and slice-thickness dependence.', [107, 108, 109, 110], 2),
    ('10.1', 'Susceptibility gradients near air-bone-brain interfaces, with phase-map illustration.', [121, 122, 123], 3),
    ('10.2', 'TE near T2* for BOLD contrast, with tradeoff schematic for sensitivity versus dropout.', [124], 1),
    ('10.3', 'Flip-angle / inflow effects on response magnitude and timing.', [126, 127, 128, 129, 130], 3),
    ('10.4', 'Receive-bias-motion interaction before and after perfect motion correction under homogeneous versus heterogeneous receive fields.', [133, 134, 135, 136], 2),
    ('11.1', 'Conjugate symmetry and partial Fourier omission of early versus late echoes.', [141, 144, 146, 147, 148, 149, 151, 155, 157, 158], 4),
    ('11.2', 'GRAPPA R=2 trajectory, ACS logic, and motion mismatch scenarios.', [159, 160, 163, 164, 165, 166, 167], 3),
    ('11.3', 'SMS acquisition and coil-based slice unaliasing.', [169, 170, 173, 175, 176, 177], 3),
    ('11.4', 'Multi-echo TE dependence for BOLD versus non-BOLD signal components.', [178, 179, 180, 181, 182], 3),
    ('11.5', 'FLEET calibration logic.', [184], 1),
    ('12.1', 'Normal ghosting reference example in EPI.', [189], 3),
    ('12.2', 'Scalp ghosts and eye-movement ghost placement.', [190, 191], 2),
    ('12.3', 'Temporal-SNR and standard-deviation images as temporal-stability tools.', [192, 199], 2),
    ('12.4', 'Residual aliasing examples for GRAPPA, SMS, and SMS + GRAPPA.', [194, 195, 196, 197], 2),
    ('12.5', 'Movement and hardware failure atlas: eyes, head, talking, feet, coil instability, metal, RF interference, gradient spikes, and RF coil spikes.', [201, 202, 203, 204, 205, 209, 210, 211, 214], 3),
    ('12.6', 'Troubleshooting decision checklist.', [216, 217], 2),
    ('13.1', 'Biological confound mechanisms and how they interact with acquisition and interpretation.', [219, 220, 221, 222, 224], 3),
    ('13.2', 'Caffeine case study showing response differences before and after dose.', [223], 1),
    ('13.3', 'MRI-based versus auxiliary-data-based confound assessment.', [225, 226], 2),
]

caption_text = {num: cap for num, cap, _, _ in FIGS}
source_caption_text = dict(caption_text)
page_map = {num: pages for num, _, pages, _ in FIGS}
path_map = {}
text_map = {}
callout_map = {}
pretitle_map = {}
presubtitle_map = {}

MANUAL_PRETITLE = {
    '5.1': 'Fourier transform: The analysis of frequency content',
    '5.2': 'The Fourier transform can determine the frequency content of complex waves',
    '5.4': '',
    '5.5': '',
    '5.8': 'The first MRI',
    '6.2': 'Slice selection also needs a refocusing gradient (echo) in practice',
    '10.2': '',
    '11.4': '',
    '11.5': 'FLEET: Fast Low-angle Excitation Echo-planar Technique',
    '13.1': '',
    '13.2': 'Caffeine: Damned if you do…?',
}

MANUAL_PRESUBTITLE = {
    '5.2': '',
    '10.2': '',
    '11.5': 'Polimeni et al. Magn Reson Med. 2016;75(2):665-679',
    '13.1': '',
    '13.2': 'Block and single trial responses to a visual task prior to and 40 minutes after a 200-mg caffeine dose. From Liu et al. (2004).',
}

MANUAL_POSTTEXT = {
    # Reserve this map for source-faithful copied slide wording only.
    # Do not add new explanatory summaries here.
    '6.2': [
        'Why? Because while Gz coincident with the RF pulse produces the slice selectivity we seek, it also has a "spoiling" (dephasing) effect. We need to undo the dephasing.',
    ],
    '9.1': [
        'Left: A delay in signal digitization relative to the read gradient periods causes rightward k-space lines to be offset relative to the leftward k-space lines.',
        'Right: Alternate kx lines after time-reversal (before 2D FT). Now we have a clear zigzag in k-space. The magnitude of the zigzag determines the intensity of the Nyquist ghosts.',
        'The error term has a ky increment twice as large as ky for the target image. Doubling dky causes the ghost image to have half the FOV as the ideal image. Hence, the ghost image "aliases," or wraps around in the FOV.',
    ],
    '9.3': [
        'Electrons in motion around a molecule generate a magnetic field that opposes B0. This shielding varies by position around the molecule.',
        '1 ppm = 123 Hz @ 2.9 T.',
    ],
    '9.4': [
        'Arises in the phase-encoded dimension, and is a result of the relatively slow sampling in that dimension.',
        'Frequency encoding axis: BW = (1/dt)/Npixels. Typically 2000-2600 Hz/pixel.',
        'Phase encoding axis: BW = (1/dtesp)/Npixels. Typically 20-35 Hz/pixel.',
        'Field heterogeneities around sinuses may be 200-300 Hz, misplacing signal in these regions by several pixels.',
    ],
    '9.5': [
        'Not strictly an EPI issue: there would be dropout for any gradient echo sequence at the same TE.',
        'But signal decay in-plane during EPI readout makes it worse.',
        'Thinner slices produce less dropout.',
        'Two thin slices > one thick slice.',
    ],
    '11.1': [
        'We should be able to omit acquisition of the early or the late echoes, with different experimental consequences.',
        'Product EPI omits early echoes. CMRR EPI allows omission of late echoes as an option.',
        'Omitting early echoes allows a shorter TE, whereas omitting later echoes allows a shorter TR.',
        'Late echo omission nets ~20% more slices in TR.',
        'Dropout may be enhanced slightly, but no new motion sensitivity is introduced.',
    ],
    '11.3': [
        'Requires a phased-array coil.',
        'Need lots of coil loops along the slice axis.',
        'Acquire a set of "single band" reference EPIs without acceleration, i.e. one multi-slice set at a time (takes SMS x TR to acquire).',
        'Then acquire time series using simultaneous slice excitation.',
        'Use a GRAPPA-like reconstruction to un-alias the simultaneous slices.',
        'Some contrast differences arise because conventional EPI can have a longer effective TR.',
        'But even SMS has limits: voxels below (2 mm)3 have low SNR, SMS > 5 is generally not advised, and one must think about R x SMS if using GRAPPA too.',
    ],
    '12.6': [
        'Assess temporal stability.',
        'Acquire a short retest.',
        'Make a brief list of possible explanations.',
        'Develop a most likely hypothesis.',
        'Does the problem exist in a different type of scan?',
        'Can you make the problem worse?',
        'Consider removing subject & setting up again.',
        'Consider running a short QC test.',
    ],
}

DOC = fitz.open(PDF_PATH)


def load_font(size: int, bold: bool = False):
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except Exception:
            pass
    return ImageFont.load_default()


TITLE_FONT = load_font(30, bold=True)
BODY_FONT = load_font(24, bold=False)
PANEL_TITLE_FONT = load_font(24, bold=True)
PANEL_SUBTITLE_FONT = load_font(20, bold=False)

SKIP_EXACT = {
    'Day One', 'Day Two', 'Day Three', 'Day Four', 'Day Five', 'Day Six',
    'Morning', 'Afternoon', 'Introduction to EPI', 'Fundamentals of MRI',
    'MRI basics', 'Advanced EPI', 'Artifacts and troubleshooting',
    'Confounds in fMRI', 'You are here!'
}
SKIP_RE = [
    re.compile(r'^https?://', re.I),
    re.compile(r'^From:\s', re.I),
    re.compile(r'^Old but useful background$', re.I),
]

OPEN_QUOTE = '\u201c'
CLOSE_QUOTE = '\u201d'
APOSTROPHE = '\u2019'
EM_DASH = '\u2014'
EN_DASH = '\u2013'
ELLIPSIS = '\u2026'
RIGHT_ARROW = '\u2192'
LEFT_RIGHT_ARROW = '\u2194'
APPROX = '\u2248'
BAD = '\ufffd'
MOJIBAKE_TRIGGERS = ''.join(
    chr(x) for x in [
        0x9225, 0x9227, 0x922b, 0x30e6, 0x63b3, 0x6502, 0x6503, 0x6508, 0x650e,
        0x6515, 0x6516, 0x6a9a, 0x6dcf, 0x6dd2, 0x6df2, 0x6e01, 0x6e02, 0x6e03,
        0x6e07, 0x6e08, 0x6e09, 0x6e0f, 0x6e13, 0x6e15, 0x6e18, 0x6e1b, 0x6e1f,
        0x6e22, 0x95b3,
    ]
)


def repair_text_surface(text: str) -> str:
    if not text:
        return ''
    if any(ch in text for ch in MOJIBAKE_TRIGGERS):
        text = text.encode('gbk', errors='replace').decode('utf-8', errors='replace')
    if BAD not in text:
        return text
    quote_pattern = re.escape(OPEN_QUOTE) + r'([^' + re.escape(CLOSE_QUOTE) + r'\n]+?)' + re.escape(BAD) + r'\?'
    text = re.sub(quote_pattern, OPEN_QUOTE + r'\1' + CLOSE_QUOTE, text)
    text = re.sub(r'([A-Za-z])' + re.escape(BAD) + re.escape(BAD) + r'([A-Za-z])', r'\1' + APOSTROPHE + r'\2', text)
    text = re.sub(r'(\*\*[^*]+\*\*) ' + re.escape(BAD) + r'\?', r'\1 ' + EM_DASH, text)
    text = re.sub(r'(\d+)' + re.escape(BAD) + r'\?(\d+)', r'\1' + EN_DASH + r'\2', text)
    replacements = {
        'CO' + BAD + '?': 'CO2',
        'T2' + BAD + '?': 'T2*',
        'TE ' + BAD + '? T2*': 'TE ' + APPROX + ' T2*',
        'TE ' + BAD + '?T2*': 'TE ' + APPROX + ' T2*',
        '- **time ' + BAD + '?frequency**': '- **time ' + LEFT_RIGHT_ARROW + ' frequency**',
        '- **space ' + BAD + '?k-space**': '- **space ' + LEFT_RIGHT_ARROW + ' k-space**',
        'neural activity ' + BAD + '?vascular and metabolic response ' + BAD + '?local susceptibility change ' + BAD + '?T2* change ' + BAD + '?MR signal change.':
            'neural activity ' + RIGHT_ARROW + ' vascular and metabolic response ' + RIGHT_ARROW + ' local susceptibility change ' + RIGHT_ARROW + ' T2* change ' + RIGHT_ARROW + ' MR signal change.',
        'head moves ' + BAD + '?tissue samples different coil sensitivity ' + BAD + '?time-varying intensity bias ' + BAD + '?realignment restores geometry but not original sensitivity weighting.':
            'head moves ' + RIGHT_ARROW + ' tissue samples different coil sensitivity ' + RIGHT_ARROW + ' time-varying intensity bias ' + RIGHT_ARROW + ' realignment restores geometry but not original sensitivity weighting.',
        'spin physics ' + BAD + '?excitation and relaxation ' + BAD + '?spatial encoding ' + BAD + '?EPI trajectory ' + BAD + '?artifact structure ' + BAD + '?motion and hardware interaction ' + BAD + '?physiologic modulation ' + BAD + '?human-factor modification ' + BAD + '?interpretation.':
            'spin physics ' + RIGHT_ARROW + ' excitation and relaxation ' + RIGHT_ARROW + ' spatial encoding ' + RIGHT_ARROW + ' EPI trajectory ' + RIGHT_ARROW + ' artifact structure ' + RIGHT_ARROW + ' motion and hardware interaction ' + RIGHT_ARROW + ' physiologic modulation ' + RIGHT_ARROW + ' human-factor modification ' + RIGHT_ARROW + ' interpretation.',
        'Damned if you do' + BAD + BAD + '?': 'Damned if you do' + ELLIPSIS + '?',
        'Damned if you do' + BAD + '?' + BAD + '?': 'Damned if you do' + ELLIPSIS + '?',
        'square ' + BAD + BAD + ' notch ' + BAD + BAD: 'square ' + OPEN_QUOTE + 'notch' + CLOSE_QUOTE,
        'Do a ' + BAD + BAD + ' mental integration ' + BAD + BAD + ' with time along the pulse sequence.':
            'Do a ' + OPEN_QUOTE + 'mental integration' + CLOSE_QUOTE + ' with time along the pulse sequence.',
        'Remember that Gy can' + BAD + BAD + 't be coincident in time with Gx (if signal is going to be recorded during Gx) or we get an oblique resultant gradient. Acquire.':
            'Remember that Gy can' + APOSTROPHE + 't be coincident in time with Gx (if signal is going to be recorded during Gx) or we get an oblique resultant gradient. Acquire.',
        'More usefully, we can sample the entire 2D k-space plane' + BAD + BAD + '.':
            'More usefully, we can sample the entire 2D k-space plane' + ELLIPSIS,
        'We will return to this seemingly arbitrary set of equations in a moment. But first' + BAD + BAD + '.':
            'We will return to this seemingly arbitrary set of equations in a moment. But first' + ELLIPSIS,
        BAD + BAD + 'Signal' + BAD + BAD + '.': OPEN_QUOTE + 'Signal' + CLOSE_QUOTE + '.',
        '2000-600 Hz/pixel': '2000-2600 Hz/pixel',
        '20-5 Hz/pixel': '20-35 Hz/pixel',
        '200-00 Hz': '200-300 Hz',
        '2000' + EN_DASH + '600 Hz/pixel': '2000-2600 Hz/pixel',
        '20' + EN_DASH + '5 Hz/pixel': '20-35 Hz/pixel',
        '200' + EN_DASH + '00 Hz': '200-300 Hz',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(re.escape(CLOSE_QUOTE) + r'(?=[A-Za-z])', CLOSE_QUOTE + ' ', text)
    text = re.sub(r'(\*\*[^*]+\*\* ' + re.escape(EM_DASH) + r')(\S)', r'\1 \2', text)
    text = text.replace('Chapters 8' + EN_DASH + '1.', 'Chapters 8' + EN_DASH + '11.')
    return text


def normalize_text(s: str) -> str:
    return re.sub(r'\s+', ' ', repair_text_surface(s or '')).strip()


def text_key(s: str) -> str:
    return re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).strip()



def is_skippable_text(line: str) -> bool:
    if not line:
        return True
    if line in SKIP_EXACT:
        return True
    for rx in SKIP_RE:
        if rx.search(line):
            return True
    return False



def clean_text_block(text: str) -> str:
    text = normalize_text(text)
    if not text:
        return ''
    # Rejoin common MRI math tokens that PDF extraction tends to split.
    replacements = {
        'B 0': 'B0',
        'B 1': 'B1',
        'T 1': 'T1',
        'T 2 *': 'T2*',
        'T 2': 'T2',
        'M xy': 'Mxy',
        'M z': 'Mz',
        'G x': 'Gx',
        'G y': 'Gy',
        'G z': 'Gz',
        'w 0': 'ω0',
        'w rot': 'ωrot',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r'\bT p\b', 'Tp', text)
    text = text.replace('x ’', 'x’').replace('y ’', 'y’').replace('z ’', 'z’')
    text = re.sub(r'\s+([,.;:!?\)])', r'\1', text)
    text = re.sub(r'\(\s+', '(', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()



def normalize_extracted_paragraph(text: str) -> str:
    text = clean_text_block(text).lstrip('•').strip()
    if not text:
        return ''
    if BAD in text:
        return ''
    if any(ch in text for ch in '∫ω𝜔𝑑𝜑𝑡'):
        return ''
    text = re.sub(r'\.{2,}', '.', text)
    if re.match(r'^https?://', text, re.I):
        return text
    if text[-1] not in '.!?':
        text += '.'
    return text



def horizontal_overlap_ratio(a, b):
    overlap = max(0, min(a.x1, b.x1) - max(a.x0, b.x0))
    return overlap / max(1, min(a.width, b.width))



def is_noise_block(text: str) -> bool:
    stripped = clean_text_block(text)
    if not stripped:
        return True
    alnum = re.sub(r'[^A-Za-z0-9]+', '', stripped)
    if len(alnum) < 3 and '=' not in stripped:
        return True
    if stripped in {'x’', 'y’', 'z’', 'x', 'y', 'z', 'B0', 'B1'}:
        return True
    return False



def extract_text_block_items(page_no: int):
    page = DOC[page_no - 1]
    blocks = page.get_text('dict').get('blocks', [])
    items = []
    for block in blocks:
        if block.get('type') != 0:
            continue
        bbox = fitz.Rect(block.get('bbox'))
        block_lines = []
        for line in block.get('lines', []):
            spans = [normalize_text(span.get('text', '')) for span in line.get('spans', [])]
            text = normalize_text(' '.join(x for x in spans if x))
            if text:
                block_lines.append(text)
        if not block_lines:
            continue
        block_text = clean_text_block(' '.join(block_lines))
        if not block_text or is_skippable_text(block_text) or is_noise_block(block_text):
            continue
        if '•' in block_text:
            parts = [clean_text_block(x) for x in block_text.split('•')]
            parts = [p for p in parts if p and not is_skippable_text(p) and not is_noise_block(p)]
            if parts:
                items.append((bbox, parts))
        else:
            items.append((bbox, [block_text]))
    return items



def extract_text_blocks_from_page(page_no: int):
    items = extract_text_block_items(page_no)
    flat = []
    for _bbox, texts in items:
        flat.extend(texts)
    seen = set()
    out = []
    for item in flat:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out



def extract_text_paragraph_items(page_no: int):
    page = DOC[page_no - 1]
    blocks = page.get_text('dict').get('blocks', [])
    items = []
    for block in blocks:
        if block.get('type') != 0:
            continue
        bbox = fitz.Rect(block.get('bbox'))
        lines = []
        for line in block.get('lines', []):
            spans = [normalize_text(span.get('text', '')) for span in line.get('spans', [])]
            text = normalize_text(' '.join(x for x in spans if x))
            if text:
                lines.append(text)
        if not lines:
            continue
        text = clean_text_block(' '.join(lines)).lstrip('•').strip()
        if not text or is_skippable_text(text) or is_noise_block(text):
            continue
        items.append((bbox, text))
    return sorted(items, key=lambda item: (item[0].y0, item[0].x0))



def merge_context_items(items):
    merged = []
    for rect, text in items:
        if merged:
            last_rect, last_text = merged[-1]
            gap = rect.y0 - last_rect.y1
            aligned = horizontal_overlap_ratio(rect, last_rect) > 0.25 or abs(rect.x0 - last_rect.x0) <= 80
            if gap <= 18 and aligned:
                merged[-1] = (rect_union([last_rect, rect]), clean_text_block(last_text + ' ' + text))
                continue
        merged.append((rect, text))
    return merged



def looks_like_heading(rect, text, page_rect):
    return bool(text) and len(text) <= 100 and rect.y0 <= page_rect.height * 0.28 and not re.search(r'https?://', text, re.I)



def extract_page_visual_info(page_no: int):
    page = DOC[page_no - 1]
    page_rect = page.rect
    blocks = page.get_text('dict').get('blocks', [])
    image_rects = [fitz.Rect(block.get('bbox')) for block in blocks if block.get('type') == 1]
    if image_rects:
        areas = [r.get_area() for r in image_rects]
        max_area = max(areas)
        filtered = [r for r in image_rects if r.get_area() >= max(max_area * 0.12, page_rect.get_area() * 0.01)]
        if not filtered:
            filtered = [image_rects[areas.index(max_area)]]
        panel_rects = [expand_region_for_content_tags(page_no, rect, include_drawings=False, pad=10) for rect in filtered]
        return {
            'mode': 'image',
            'panel_rects': panel_rects,
            'visual_union': rect_union(panel_rects),
        }
    if is_low_info_title_page(page_no):
        return {'mode': 'none', 'panel_rects': [], 'visual_union': None}
    drawing_rects = [fitz.Rect(drawing.get('rect')) for drawing in page.get_drawings() if drawing.get('rect')]
    if len(drawing_rects) > 2:
        drawing_union = rect_union(drawing_rects)
        label_rects = []
        for rect, _text in extract_text_paragraph_items(page_no):
            vertical_gap = 0
            if rect.y1 < drawing_union.y0:
                vertical_gap = drawing_union.y0 - rect.y1
            elif rect.y0 > drawing_union.y1:
                vertical_gap = rect.y0 - drawing_union.y1
            if rect.intersects(drawing_union) or (horizontal_overlap_ratio(rect, drawing_union) > 0.2 and vertical_gap <= 28):
                label_rects.append(rect)
        content = rect_union(drawing_rects + label_rects)
        if content is not None:
            return {
                'mode': 'vector',
                'panel_rects': [padded(content, page_rect, pad=10)],
                'visual_union': content,
            }
    return {'mode': 'none', 'panel_rects': [], 'visual_union': None}



def extract_panel_context(page_no: int, visual_info):
    page = DOC[page_no - 1]
    page_rect = page.rect
    items = extract_text_paragraph_items(page_no)
    if not items:
        return {'title': '', 'subtitle': '', 'post_lines': []}

    used = set()
    title = ''
    title_rect = None
    first_rect, first_text = items[0]
    if looks_like_heading(first_rect, first_text, page_rect):
        title = first_text
        title_rect = first_rect
        used.add(0)

    subtitle_parts = []
    subtitle_rects = []
    if title_rect is not None:
        title_center = (title_rect.x0 + title_rect.x1) / 2
        for idx in range(1, len(items)):
            rect, text = items[idx]
            if idx in used:
                continue
            if rect.y0 > min((visual_info.get('visual_union') or page_rect).y0 + 20, page_rect.height * 0.42):
                break
            rect_center = (rect.x0 + rect.x1) / 2
            aligned = abs(rect_center - title_center) <= page_rect.width * 0.14 or abs(rect.x0 - title_rect.x0) <= 90
            close = not subtitle_rects or (
                rect.y0 - subtitle_rects[-1].y1 <= 24 and
                (abs(rect.x0 - subtitle_rects[-1].x0) <= 90 or abs(rect_center - ((subtitle_rects[-1].x0 + subtitle_rects[-1].x1) / 2)) <= page_rect.width * 0.14)
            )
            if aligned and close and len(text) <= 140 and not re.search(r'https?://', text, re.I):
                subtitle_parts.append(text)
                subtitle_rects.append(rect)
                used.add(idx)
                continue
            break
    subtitle = clean_text_block(' '.join(subtitle_parts))

    post_candidates = []
    visual_union = visual_info.get('visual_union')
    for idx, (rect, text) in enumerate(items):
        if idx in used:
            continue
        if title_rect is not None and text_key(text) == text_key(title):
            continue
        if subtitle and text_key(text) == text_key(subtitle):
            continue
        if visual_info.get('mode') == 'image' and visual_union is not None and rect.intersects(padded(visual_union, page_rect, pad=10)):
            continue
        post_candidates.append((rect, text))

    merged_post = merge_context_items(post_candidates)
    seen = set()
    post_lines = []
    skip_keys = {text_key(title), text_key(subtitle)}
    for _rect, text in merged_post:
        normalized = normalize_extracted_paragraph(text)
        key = text_key(normalized)
        alpha_chars = len(re.findall(r'[A-Za-z]', normalized))
        if not normalized or not key or key in seen or key in skip_keys:
            continue
        if len(normalized) <= 18 and alpha_chars < 6 and not re.match(r'^https?://', normalized, re.I):
            continue
        seen.add(key)
        post_lines.append(normalized)

    return {'title': title, 'subtitle': subtitle, 'post_lines': post_lines}


def normalize_callouts_for_figure(fig_num: str, paragraphs):
    cleaned = []
    seen = set()
    skip = {
        text_key(caption_text.get(fig_num, '')),
        text_key(pretitle_map.get(fig_num, '')),
        text_key(presubtitle_map.get(fig_num, '')),
    }
    for paragraph in paragraphs:
        normalized = normalize_extracted_paragraph(paragraph)
        key = text_key(normalized)
        if not key or key in seen or key in skip:
            continue
        seen.add(key)
        cleaned.append(normalized)
    return cleaned


def extract_source_text_pages(page_nos):
    paragraphs = []
    for page_no in page_nos:
        context = extract_panel_context(page_no, {'mode': 'none', 'visual_union': None})
        title = clean_text_block(context.get('title', ''))
        subtitle = clean_text_block(context.get('subtitle', ''))
        if title:
            paragraphs.append(title)
        if subtitle:
            paragraphs.append(subtitle)
        paragraphs.extend(context.get('post_lines', []))
    return paragraphs


def extract_source_header(page_no: int):
    context = extract_panel_context(page_no, {'mode': 'none', 'visual_union': None})
    return clean_text_block(context.get('title', '')), clean_text_block(context.get('subtitle', ''))



def wrap_text_lines(draw, text, font, width_px):
    words = text.split()
    lines = []
    current = ''
    for word in words:
        test = (current + ' ' + word).strip()
        if not current or draw.textlength(test, font=font) <= width_px:
            current = test
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines



def decorate_panel_image(img, title='', subtitle=''):
    title = clean_text_block(title)
    subtitle = clean_text_block(subtitle)
    if not title and not subtitle:
        return img
    scratch = Image.new('RGB', (img.width, 10), 'white')
    draw = ImageDraw.Draw(scratch)
    text_width = max(200, img.width - 40)
    title_lines = wrap_text_lines(draw, title, PANEL_TITLE_FONT, text_width) if title else []
    subtitle_lines = wrap_text_lines(draw, subtitle, PANEL_SUBTITLE_FONT, text_width) if subtitle else []
    header_h = 20
    if title_lines:
        header_h += len(title_lines) * 34
    if subtitle_lines:
        header_h += len(subtitle_lines) * 28 + 6
    header_h += 16
    canvas = Image.new('RGB', (img.width, img.height + header_h), 'white')
    canvas.paste(img, (0, header_h))
    draw = ImageDraw.Draw(canvas)
    y = 14
    for line in title_lines:
        bbox = draw.textbbox((0, 0), line, font=PANEL_TITLE_FONT)
        draw.text(((img.width - (bbox[2] - bbox[0])) / 2, y), line, font=PANEL_TITLE_FONT, fill='black')
        y += 34
    if title_lines and subtitle_lines:
        y += 2
    for line in subtitle_lines:
        bbox = draw.textbbox((0, 0), line, font=PANEL_SUBTITLE_FONT)
        draw.text(((img.width - (bbox[2] - bbox[0])) / 2, y), line, font=PANEL_SUBTITLE_FONT, fill=(45, 45, 45))
        y += 28
    draw.line((12, header_h - 8, img.width - 12, header_h - 8), fill=(215, 215, 215), width=2)
    return canvas



def is_low_info_title_page(page_no: int) -> bool:
    page = DOC[page_no - 1]
    blocks = extract_text_blocks_from_page(page_no)
    image_count = len(page.get_images(full=True))
    drawing_count = len(page.get_drawings())
    if image_count > 0:
        return False
    if drawing_count > 2:
        return False
    if len(blocks) <= 3:
        joined = ' '.join(blocks)
        if len(joined) <= 80:
            return True
    return False



def rect_union(rects):
    rects = [fitz.Rect(r) for r in rects if r is not None]
    if not rects:
        return None
    rect = fitz.Rect(rects[0])
    for r in rects[1:]:
        rect |= fitz.Rect(r)
    return rect



def padded(rect, page_rect, pad=12):
    r = fitz.Rect(rect)
    r.x0 -= pad
    r.y0 -= pad
    r.x1 += pad
    r.y1 += pad
    return r & page_rect



def near_image_text_blocks(image_union, text_items):
    selected = []
    expanded = fitz.Rect(image_union)
    expanded.x0 -= 60
    expanded.x1 += 60
    expanded.y0 -= 90
    expanded.y1 += 90
    for rect, texts in text_items:
        horiz_overlap = max(0, min(rect.x1, expanded.x1) - max(rect.x0, expanded.x0))
        horiz_ratio = horiz_overlap / max(1, min(rect.width, image_union.width))
        vertical_gap = 0
        if rect.y1 < image_union.y0:
            vertical_gap = image_union.y0 - rect.y1
        elif rect.y0 > image_union.y1:
            vertical_gap = rect.y0 - image_union.y1
        if rect.intersects(expanded) or (horiz_ratio > 0.22 and vertical_gap <= 110):
            selected.append((rect, texts))
    return selected


def rect_gap(a, b):
    horizontal_gap = 0
    if a.x1 < b.x0:
        horizontal_gap = b.x0 - a.x1
    elif b.x1 < a.x0:
        horizontal_gap = a.x0 - b.x1
    vertical_gap = 0
    if a.y1 < b.y0:
        vertical_gap = b.y0 - a.y1
    elif b.y1 < a.y0:
        vertical_gap = a.y0 - b.y1
    return horizontal_gap, vertical_gap


def rect_close_to_region(rect, region, max_hgap=150, max_vgap=160):
    rect = fitz.Rect(rect)
    region = fitz.Rect(region)
    hgap, vgap = rect_gap(rect, region)
    horiz_overlap = max(0, min(rect.x1, region.x1) - max(rect.x0, region.x0))
    vert_overlap = max(0, min(rect.y1, region.y1) - max(rect.y0, region.y0))
    return (
        rect.intersects(region)
        or (horiz_overlap > 0 and vgap <= max_vgap)
        or (vert_overlap > 0 and hgap <= max_hgap)
        or (hgap <= 90 and vgap <= 90)
    )


def expand_region_for_content_tags(page_no: int, region, include_drawings: bool = True, pad: int = 12):
    page = DOC[page_no - 1]
    page_rect = page.rect
    region = fitz.Rect(region) & page_rect
    tag_rects = []
    for rect, text in extract_text_paragraph_items(page_no):
        if looks_like_heading(rect, text, page_rect):
            continue
        if len(text) > 140:
            continue
        if rect_close_to_region(rect, region):
            tag_rects.append(rect)
    drawing_rects = []
    if include_drawings:
        for drawing in page.get_drawings():
            rect = drawing.get('rect')
            if not rect:
                continue
            rect = fitz.Rect(rect)
            if rect_close_to_region(rect, region, max_hgap=110, max_vgap=110):
                drawing_rects.append(rect)
    content = rect_union([region] + tag_rects + drawing_rects)
    return padded(content or region, page_rect, pad=pad)



def extract_visual_regions(page_no: int):
    page = DOC[page_no - 1]
    page_rect = page.rect
    blocks = page.get_text('dict').get('blocks', [])
    image_rects = []
    text_rects = []
    for block in blocks:
        btype = block.get('type')
        bbox = fitz.Rect(block.get('bbox'))
        if btype == 1:
            image_rects.append(bbox)
        elif btype == 0:
            block_lines = []
            for line in block.get('lines', []):
                spans = [normalize_text(span.get('text', '')) for span in line.get('spans', [])]
                text = normalize_text(' '.join(x for x in spans if x))
                if text:
                    block_lines.append(text)
            block_text = clean_text_block(' '.join(block_lines)) if block_lines else ''
            if block_text and not is_skippable_text(block_text) and not is_noise_block(block_text):
                text_rects.append((bbox, [block_text]))

    drawing_rects = []
    for drawing in page.get_drawings():
        rect = drawing.get('rect')
        if rect:
            drawing_rects.append(fitz.Rect(rect))

    # Prefer actual embedded images, but include nearby labels/captions that belong to them.
    if image_rects:
        areas = [r.get_area() for r in image_rects]
        max_area = max(areas)
        filtered = [r for r in image_rects if r.get_area() >= max(max_area * 0.12, page_rect.get_area() * 0.01)]
        if not filtered:
            filtered = [image_rects[areas.index(max_area)]]
        combined_images = rect_union(filtered)
        nearby_text = near_image_text_blocks(combined_images, text_rects)
        content = rect_union(filtered + [rect for rect, _texts in nearby_text])
        if content is not None:
            return [expand_region_for_content_tags(page_no, content, include_drawings=False, pad=10)]
        return []

    # Pure text / title slides should not become figure panels.
    if is_low_info_title_page(page_no):
        return []

    # For vector-diagram slides, crop the diagram region plus nearby labels only.
    if len(drawing_rects) > 2:
        content = rect_union(drawing_rects + [rect for rect, _texts in text_rects])
        if content is not None:
            return [padded(content, page_rect, pad=14)]

    # Otherwise this is probably a text slide: extract text only, no visual crop.
    return []



def extract_image_callouts(page_no: int):
    page = DOC[page_no - 1]
    page_rect = page.rect
    image_rects = [fitz.Rect(block.get('bbox')) for block in page.get_text('dict').get('blocks', []) if block.get('type') == 1]
    if not image_rects:
        return []
    areas = [r.get_area() for r in image_rects]
    max_area = max(areas)
    filtered = [r for r in image_rects if r.get_area() >= max(max_area * 0.12, page_rect.get_area() * 0.01)]
    if not filtered:
        filtered = [image_rects[areas.index(max_area)]]
    image_union = rect_union(filtered)
    nearby = near_image_text_blocks(image_union, extract_text_block_items(page_no))
    callouts = []
    for _rect, texts in nearby:
        for t in texts:
            t = clean_text_block(t)
            if t and len(t) <= 110:
                callouts.append(t)
    seen = set()
    out = []
    for t in callouts:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out[:5]



def crop_page(page_no: int, bbox, zoom: float = 2.8):
    page = DOC[page_no - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(bbox), alpha=False)
    img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
    framed = Image.new('RGB', (img.width + 8, img.height + 8), 'white')
    framed.paste(img, (4, 4))
    draw = ImageDraw.Draw(framed)
    draw.rectangle((1, 1, framed.width - 2, framed.height - 2), outline=(180, 180, 180), width=2)
    return framed



def fractional_bbox(page_no: int, left: float, top: float, right: float, bottom: float):
    page_rect = DOC[page_no - 1].rect
    return fitz.Rect(
        page_rect.x0 + page_rect.width * left,
        page_rect.y0 + page_rect.height * top,
        page_rect.x0 + page_rect.width * right,
        page_rect.y0 + page_rect.height * bottom,
    )


def override_figure_with_custom_crops(
    num: str,
    crop_specs,
    cols: int = 1,
    chunk_size=None,
    text_pages=None,
    pretitle: str = '',
    presubtitle: str = '',
):
    panels = []
    seen = set()
    extracted = []
    for spec in crop_specs:
        page_no = spec['page']
        bbox = fractional_bbox(page_no, *spec['crop'])
        if spec.get('preserve_tags', True):
            bbox = expand_region_for_content_tags(
                page_no,
                bbox,
                include_drawings=spec.get('include_drawings', True),
                pad=spec.get('pad', 12),
            )
        img = crop_page(page_no, bbox, zoom=spec.get('zoom', 2.8))
        panel_title = clean_text_block(spec.get('title', ''))
        panel_subtitle = clean_text_block(spec.get('subtitle', ''))
        if panel_title or panel_subtitle:
            img = decorate_panel_image(img, title=panel_title, subtitle=panel_subtitle)
        panels.append({'img': img})
    for page_no in (text_pages or sorted({spec['page'] for spec in crop_specs})):
        for line in extract_text_blocks_from_page(page_no):
            if line not in seen:
                seen.add(line)
                extracted.append(line)
    if chunk_size is None and len(panels) > 2:
        chunk_size = 2
    save_figure_panels(num, panels, cols=cols, chunk_size=chunk_size)
    caption_text[num] = source_caption_text.get(num, caption_text.get(num, ''))
    text_map[num] = extracted
    pretitle_map[num] = clean_text_block(pretitle)
    presubtitle_map[num] = clean_text_block(presubtitle)


def make_grid(panels, cols, bg=(255, 255, 255), gutter=24, outer=24):
    target_panel_w = {1: 1500, 2: 900, 3: 620, 4: 460}.get(cols, 620)
    rendered = []
    for panel in panels:
        img = panel['img']
        ratio = target_panel_w / img.width
        h = int(img.height * ratio)
        resized = img.resize((target_panel_w, h), Image.LANCZOS)
        rendered.append(resized)
    if len(rendered) == 1:
        return rendered[0]

    rows = math.ceil(len(rendered) / cols)
    row_heights = []
    idx = 0
    for _ in range(rows):
        current = rendered[idx:idx + cols]
        row_heights.append(max(im.height for im in current))
        idx += cols

    canvas_w = outer * 2 + cols * target_panel_w + gutter * (cols - 1)
    canvas_h = outer * 2 + sum(row_heights) + gutter * (rows - 1)
    canvas = Image.new('RGB', (canvas_w, canvas_h), bg)

    idx = 0
    y = outer
    for row_h in row_heights:
        x = outer
        for _ in range(cols):
            if idx >= len(rendered):
                break
            img = rendered[idx]
            yy = y + (row_h - img.height) // 2
            canvas.paste(img, (x, yy))
            x += target_panel_w + gutter
            idx += 1
        y += row_h + gutter
    return canvas


def save_figure_panels(num: str, panels, cols: int = 1, chunk_size=None):
    if not panels:
        return None
    cols = max(1, min(cols, 2))
    chunk_size = chunk_size or len(panels)
    rel_paths = []
    prefix = f"figure_{num.replace('.', '_')}"
    for old_path in FIG_DIR.glob(f'{prefix}*.png'):
        old_path.unlink(missing_ok=True)
    for chunk_idx, start in enumerate(range(0, len(panels), chunk_size), start=1):
        chunk = panels[start:start + chunk_size]
        composite = make_grid(chunk, cols=min(cols, len(chunk)))
        suffix = '' if len(panels) <= chunk_size else f'_{chunk_idx}'
        fname = f"figure_{num.replace('.', '_')}{suffix}.png"
        composite.save(FIG_DIR / fname, optimize=True)
        rel_paths.append(f'figures/{fname}')
    path_map[num] = rel_paths[0] if len(rel_paths) == 1 else rel_paths
    return path_map[num]


# Source-backed figures: crop actual visual regions instead of whole slides.
# Keep all informative panels by default, but favor readable one- or two-column layouts.
for num, caption, pages, cols in FIGS:
    panel_entries = []
    figure_lines = []
    for p in pages:
        figure_lines.extend(extract_text_blocks_from_page(p))
        visual_info = extract_page_visual_info(p)
        if not visual_info.get('panel_rects'):
            continue
        context = extract_panel_context(p, visual_info)
        for bbox in visual_info['panel_rects']:
            rect = fitz.Rect(bbox)
            panel_entries.append({
                'area': rect.get_area(),
                'page': p,
                'img': crop_page(p, bbox),
                'title': context.get('title', ''),
                'subtitle': context.get('subtitle', ''),
                'post_lines': list(context.get('post_lines', [])),
            })
    seen = set()
    deduped = []
    for line in figure_lines:
        if line not in seen:
            seen.add(line)
            deduped.append(line)
    text_map[num] = deduped
    callout_map[num] = []
    pretitle_map[num] = ''
    presubtitle_map[num] = ''
    if panel_entries:
        chosen = sorted(panel_entries, key=lambda item: (item['page'], -item['area']))
        chosen = sorted(chosen, key=lambda item: item['page'])
        generic_chunk_size = 2 if len(chosen) > 2 else None
        save_figure_panels(num, chosen, cols=min(2, cols, len(chosen)), chunk_size=generic_chunk_size)

        if len(chosen) == 1:
            pretitle_map[num] = clean_text_block(chosen[0].get('title', ''))
            presubtitle_map[num] = clean_text_block(chosen[0].get('subtitle', ''))

        if num in MANUAL_PRETITLE:
            pretitle_map[num] = clean_text_block(MANUAL_PRETITLE[num])
        if num in MANUAL_PRESUBTITLE:
            presubtitle_map[num] = clean_text_block(MANUAL_PRESUBTITLE[num])

        post_lines = []
        seen_post = set()
        skip_keys = {text_key(caption_text.get(num, caption)), text_key(caption), text_key(pretitle_map[num]), text_key(presubtitle_map[num])}
        for entry in chosen:
            for line in entry.get('post_lines', []):
                key = text_key(line)
                if not key or key in seen_post or key in skip_keys:
                    continue
                if entry.get('title') and key == text_key(entry['title']):
                    continue
                if entry.get('subtitle') and key == text_key(entry['subtitle']):
                    continue
                seen_post.add(key)
                post_lines.append(line)
        callout_map[num] = normalize_callouts_for_figure(num, post_lines)


# Replace weak remaining slide-derived figures with cleaner textbook-style originals where needed.
# Figure 3.2: textbook recovery/decay curves to replace the bad chemical-shift mismatch.
img = Image.new('RGB', (1800, 920), 'white')
draw = ImageDraw.Draw(img)
draw.text((70, 55), 'Figure 3.2. Longitudinal recovery and transverse decay curves with T1, T2, and T2* annotated.', font=TITLE_FONT, fill='black')

# Left panel: T1 recovery.
draw.rounded_rectangle((90, 160, 860, 790), radius=26, outline='black', width=3, fill=(248, 250, 253))
draw.text((120, 190), 'Longitudinal recovery (T1)', font=TITLE_FONT, fill='black')
# axes
x0, y0 = 180, 700
x1, y1 = 780, 300
draw.line((x0, y0, x0, y1), fill='black', width=4)
draw.line((x0, y0, x1, y0), fill='black', width=4)
draw.text((790, 684), 'time', font=BODY_FONT, fill='black')
draw.text((140, 255), 'Mz', font=BODY_FONT, fill='black')
# grid + M0 line
for frac in [0.25, 0.5, 0.75, 1.0]:
    yy = y0 - int((y0 - y1) * frac)
    draw.line((x0, yy, x1, yy), fill=(220, 224, 229), width=2)
draw.line((x0, y1, x1, y1), fill=(120, 120, 120), width=2)
draw.text((x1 - 45, y1 - 32), 'M0', font=BODY_FONT, fill=(80, 80, 80))
# exponential recovery curve
pts = []
for i in range(0, 401):
    t = i / 400 * 4.0
    val = 1.0 - math.exp(-t / 1.1)
    x = x0 + int((x1 - x0) * i / 400)
    y = y0 - int((y0 - y1) * val)
    pts.append((x, y))
draw.line(pts, fill=(40, 100, 210), width=7)
# T1 marker at 63%
t1_t = 1.1
x_t1 = x0 + int((x1 - x0) * (t1_t / 4.0))
y_t1 = y0 - int((y0 - y1) * (1.0 - math.exp(-1)))
draw.line((x_t1, y0, x_t1, y_t1), fill=(200, 90, 0), width=4)
draw.line((x0, y_t1, x_t1, y_t1), fill=(200, 90, 0), width=4)
draw.ellipse((x_t1 - 10, y_t1 - 10, x_t1 + 10, y_t1 + 10), fill=(200, 90, 0), outline='black')
draw.text((x_t1 + 18, y_t1 - 35), 'T1 ≈ 63% recovery', font=BODY_FONT, fill=(170, 70, 0))
draw.text((130, 735), 'After excitation, Mz regrows toward equilibrium M0.', font=BODY_FONT, fill='black')

# Right panel: T2/T2* decay.
draw.rounded_rectangle((940, 160, 1710, 790), radius=26, outline='black', width=3, fill=(248, 250, 253))
draw.text((970, 190), 'Transverse decay (T2 and T2*)', font=TITLE_FONT, fill='black')
x0, y0 = 1030, 700
x1, y1 = 1630, 300
draw.line((x0, y0, x0, y1), fill='black', width=4)
draw.line((x0, y0, x1, y0), fill='black', width=4)
draw.text((1640, 684), 'time', font=BODY_FONT, fill='black')
draw.text((980, 255), 'Mxy', font=BODY_FONT, fill='black')
for frac in [0.25, 0.5, 0.75, 1.0]:
    yy = y0 - int((y0 - y1) * frac)
    draw.line((x0, yy, x1, yy), fill=(220, 224, 229), width=2)
# T2 curve
pts_t2 = []
pts_t2s = []
for i in range(0, 401):
    t = i / 400 * 4.0
    val_t2 = math.exp(-t / 1.6)
    val_t2s = math.exp(-t / 0.85)
    x = x0 + int((x1 - x0) * i / 400)
    y_t2 = y0 - int((y0 - y1) * val_t2)
    y_t2s = y0 - int((y0 - y1) * val_t2s)
    pts_t2.append((x, y_t2))
    pts_t2s.append((x, y_t2s))
draw.line(pts_t2, fill=(40, 140, 80), width=7)
draw.line(pts_t2s, fill=(190, 55, 55), width=7)
draw.text((1325, 395), 'T2 (slower)', font=BODY_FONT, fill=(30, 120, 65))
draw.text((1165, 520), 'T2* (faster)', font=BODY_FONT, fill=(170, 45, 45))
draw.text((980, 724), 'T2* < T2 because field inhomogeneity adds extra dephasing.', font=BODY_FONT, fill='black')

img.save(FIG_DIR / 'figure_3_2.png')
path_map['3.2'] = 'figures/figure_3_2.png'
caption_text['3.2'] = 'Longitudinal recovery and transverse decay curves with T1, T2, and T2* annotated.'
callout_map['3.2'] = []
text_map['3.2'] = [
    'Left panel: longitudinal recovery Mz(t) toward M0, showing T1 as the recovery time constant.',
    'Right panel: transverse decay Mxy(t), with T2* decaying faster than T2 because microscopic spin-spin effects and macroscopic field inhomogeneity both contribute.',
]

# Keep the underlying extracted hardware-component bullets in the validation artifact only.
text_map['4.1'] = [
    'Main MRI components',
    '3 T magnet to polarize the subject',
    '3-axis gradient coils to encode spatial info. (max. 80 mT/m)',
    '123 MHz transmit RF coil to excite spins (max. ~20 μT)',
    '123 MHz receive-only coil',
    '(We use a body coil to transmit B1, separate head coil to receive.)',
]

# Remove misleading extracted titles/subtitles that really belong to the following figure rather than the current one.
presubtitle_map['4.2'] = ''
presubtitle_map['5.1'] = ''
presubtitle_map['5.4'] = ''
presubtitle_map['5.7'] = ''
presubtitle_map['6.1'] = ''
presubtitle_map['11.4'] = ''
presubtitle_map['13.1'] = ''
pretitle_map['11.4'] = ''
pretitle_map['13.1'] = ''

# Reassert only explicit source-faithful posttext and title overrides after later figure-specific adjustments.
for fig_num, paragraphs in MANUAL_POSTTEXT.items():
    callout_map[fig_num] = normalize_callouts_for_figure(fig_num, paragraphs)
for fig_num, title in MANUAL_PRETITLE.items():
    pretitle_map[fig_num] = clean_text_block(title)
for fig_num, subtitle in MANUAL_PRESUBTITLE.items():
    presubtitle_map[fig_num] = clean_text_block(subtitle)

# Remove very short or clearly broken extracted titles/subtitles after the final override pass.
for fig_num in list(pretitle_map.keys()):
    title = clean_text_block(pretitle_map.get(fig_num, ''))
    if len(re.findall(r'[A-Za-z]', title)) < 4:
        pretitle_map[fig_num] = ''
for fig_num in list(presubtitle_map.keys()):
    subtitle = clean_text_block(presubtitle_map.get(fig_num, ''))
    if len(re.findall(r'[A-Za-z]', subtitle)) < 6:
        presubtitle_map[fig_num] = ''

# Keep captions from becoming duplicate post-figure text.
for fig_num, paragraphs in list(callout_map.items()):
    callout_map[fig_num] = normalize_callouts_for_figure(fig_num, paragraphs)


FULL_PAGE_FIG_OVERRIDES = {
    '1.1': 1,
    '2.1': 1,
    '2.2': 1,
    '2.3': 1,
    '2.4': 1,
    '3.1': 1,
    '3.2': 1,
    '3.3': 1,
    '3.4': 1,
    '3.5': 1,
    '3.6': 1,
    '3.7': 1,
    '3.8': 1,
    '4.1': 1,
    '4.2': 1,
    '4.3': 1,
    '4.4': 1,
    '10.4': 2,
    '12.5': 3,
}


def override_figure_with_full_pages(num: str, cols: int = 1, zoom: float = 2.2, pages=None, chunk_size=None):
    pages = list(pages or page_map.get(num, []))
    panels = []
    extracted = []
    seen = set()
    for page_no in pages:
        page = DOC[page_no - 1]
        panels.append({'img': crop_page(page_no, page.rect, zoom=zoom)})
        for line in extract_text_blocks_from_page(page_no):
            if line not in seen:
                seen.add(line)
                extracted.append(line)
    if not panels:
        return
    save_figure_panels(num, panels, cols=cols, chunk_size=chunk_size)
    caption_text[num] = source_caption_text.get(num, caption_text.get(num, ''))
    callout_map[num] = []
    pretitle_map[num] = ''
    presubtitle_map[num] = ''
    text_map[num] = extracted


def override_figure_with_mixed_pages(
    num: str,
    visual_pages,
    text_pages=None,
    title_pages=None,
    cols: int = 1,
    zoom: float = 2.2,
    chunk_size=None,
):
    visual_pages = list(visual_pages)
    text_pages = list(text_pages or [])
    title_pages = list(title_pages or [])
    panels = []
    extracted = []
    seen = set()
    for page_no in title_pages + visual_pages + text_pages:
        for line in extract_text_blocks_from_page(page_no):
            if line not in seen:
                seen.add(line)
                extracted.append(line)
    for page_no in visual_pages:
        page = DOC[page_no - 1]
        panels.append({'img': crop_page(page_no, page.rect, zoom=zoom)})
    if not panels:
        return
    save_figure_panels(num, panels, cols=cols, chunk_size=chunk_size)
    caption_text[num] = source_caption_text.get(num, caption_text.get(num, ''))
    text_map[num] = extracted
    pretitle_map[num] = ''
    presubtitle_map[num] = ''
    if title_pages:
        title, subtitle = extract_source_header(title_pages[0])
        pretitle_map[num] = title
        presubtitle_map[num] = subtitle
    callout_map[num] = normalize_callouts_for_figure(num, extract_source_text_pages(text_pages))


for fig_num, cols in FULL_PAGE_FIG_OVERRIDES.items():
    override_figure_with_full_pages(fig_num, cols=cols)

# Figure 6.1: slice-selection bandwidth / thickness summary.
img = Image.new('RGB', (1800, 900), 'white')
draw = ImageDraw.Draw(img)
draw.text((70, 55), 'Figure 6.1. Slice selection and slice thickness.', font=TITLE_FONT, fill='black')
# Left panel: bandwidth maps to slice thickness.
draw.rounded_rectangle((90, 160, 860, 760), radius=26, outline='black', width=3, fill=(248, 250, 253))
draw.text((120, 190), 'Frequency-selective RF pulse under Gz', font=TITLE_FONT, fill='black')
draw.line((260, 300, 260, 650), fill='black', width=4)
draw.line((210, 600, 760, 600), fill='black', width=4)
draw.text((770, 585), 'z', font=BODY_FONT, fill='black')
draw.text((235, 260), 'frequency', font=BODY_FONT, fill='black')
draw.line((310, 370, 700, 370), fill=(80,80,80), width=16)
draw.line((505, 260, 505, 650), fill=(60,60,60), width=3)
draw.line((310, 600, 700, 300), fill=(40,40,40), width=5)
draw.line((310, 430, 700, 430), fill=(180,120,0), width=6)
draw.line((380, 390, 380, 470), fill=(180,120,0), width=4)
draw.line((640, 390, 640, 470), fill=(180,120,0), width=4)
draw.text((470, 445), 'Δν', font=BODY_FONT, fill=(160,100,0))
draw.text((520, 500), 'Selected band', font=BODY_FONT, fill='black')
draw.text((120, 675), 'Key idea: under Gz, RF bandwidth Δν', font=BODY_FONT, fill='black')
draw.text((120, 715), 'sets the slice thickness Δz.', font=BODY_FONT, fill='black')
# Right panel: thick vs thin slice.
draw.rounded_rectangle((940, 160, 1710, 760), radius=26, outline='black', width=3, fill=(248, 250, 253))
draw.text((970, 190), 'Changing slice thickness', font=TITLE_FONT, fill='black')
for x, y, scale in [(1080, 400, 1.0), (1440, 400, 0.65)]:
    w = int(130 * scale)
    h = int(250 * scale)
    draw.ellipse((x-w//2, y-h//2, x+w//2, y-h//2 + 55*scale), fill=(120,150,255), outline='black')
    draw.rectangle((x-w//2, y-h//2 + 25*scale, x+w//2, y+h//2 - 25*scale), fill=(120,150,255), outline='black')
    draw.ellipse((x-w//2, y+h//2 - 55*scale, x+w//2, y+h//2), fill=(90,120,235), outline='black')
    draw.rectangle((x-15, y-160, x+15, y+160), outline=(230, 180, 0), width=4)
draw.text((960, 620), 'broader RF band or', font=BODY_FONT, fill='black')
draw.text((960, 658), 'smaller Gz → thicker slice', font=BODY_FONT, fill='black')
draw.text((1280, 620), 'narrower RF band or', font=BODY_FONT, fill='black')
draw.text((1280, 658), 'larger Gz → thinner slice', font=BODY_FONT, fill='black')
img.save(FIG_DIR / 'figure_6_1.png', optimize=True)
path_map['6.1'] = 'figures/figure_6_1.png'
caption_text['6.1'] = 'Sinc-shaped RF pulse and rectangular excitation bandwidth, showing frequency-selective slice selection under Gz.'
text_map['6.1'] = [
    'The notch of frequencies Δν corresponds to a spatial notch of width Δz.',
    'This is a slice, of thickness Δz.',
    'To change slice thickness we can change Gz.',
    'If we double Gz we halve the slice thickness.',
]

# Figure 6.3: keep the original gradient-echo slides so the stage labels, formulas, and visual tags remain inside the figure.
gradient_panels = []
for page_no in [50, 51, 52]:
    regions = extract_visual_regions(page_no)
    if not regions:
        continue
    gradient_panels.append({
        'img': crop_page(page_no, regions[0]),
    })
if gradient_panels:
    composite = make_grid(gradient_panels, cols=1)
    composite.save(FIG_DIR / 'figure_6_3.png', optimize=True)
    path_map['6.3'] = 'figures/figure_6_3.png'
    caption_text['6.3'] = 'Three-stage gradient-echo formation sequence.'
    text_map['6.3'] = []
    for page_no in [50, 51, 52]:
        for line in extract_text_blocks_from_page(page_no):
            if line not in text_map['6.3']:
                text_map['6.3'].append(line)

# Figure 7.3: k-space matrix-building summary.
img = Image.new('RGB', (1800, 900), 'white')
draw = ImageDraw.Draw(img)
draw.text((70, 55), 'Figure 7.3. Building a 2D k-space matrix line by line.', font=TITLE_FONT, fill='black')
draw.rounded_rectangle((90, 160, 760, 760), radius=26, outline='black', width=3, fill=(248, 250, 253))
draw.text((120, 190), 'One repetition of the sequence', font=TITLE_FONT, fill='black')
labels = ['RF', 'Gz', 'Gy', 'Gx']
ys = [300, 390, 480, 570]
for lab, y in zip(labels, ys):
    draw.text((130, y-18), lab, font=BODY_FONT, fill='black')
    draw.line((210, y, 690, y), fill='black', width=3)
draw.rectangle((270, 270, 330, 330), outline='black', width=3)
draw.text((280, 282), '90°', font=BODY_FONT, fill='black')
draw.polygon([(280, 390), (360, 330), (440, 390)], outline='black', width=3)
draw.polygon([(470, 480), (540, 420), (610, 480)], outline='black', width=3)
draw.rectangle((300, 540, 620, 600), outline='black', width=3)
draw.text((120, 670), 'Slice select → one phase-encode step → one k-space line', font=BODY_FONT, fill='black')
draw.rounded_rectangle((910, 160, 1710, 760), radius=26, outline='black', width=3, fill=(248, 250, 253))
draw.text((940, 190), 'Repeated phase-encode steps fill k-space', font=TITLE_FONT, fill='black')
# k-space grid
x0, y0, step = 1010, 300, 40
for i in range(9):
    draw.line((x0, y0+i*step, x0+8*step, y0+i*step), fill=(170,170,170), width=2)
    draw.line((x0+i*step, y0, x0+i*step, y0+8*step), fill=(170,170,170), width=2)
# Highlight sampled lines.
for idx, color in zip([1, 3, 4, 6, 7], [(220,60,60), (60,120,220), (220,160,0), (60,160,100), (140,80,200)]):
    draw.line((x0, y0+idx*step, x0+8*step, y0+idx*step), fill=color, width=6)
    draw.polygon([(x0+8*step+8, y0+idx*step), (x0+8*step-10, y0+idx*step-8), (x0+8*step-10, y0+idx*step+8)], fill=color)
draw.text((1010, 670), 'Each repetition stores one row at a new ky value.', font=BODY_FONT, fill='black')
draw.text((1010, 710), 'After all rows are filled, the 2D Fourier transform gives the image.', font=BODY_FONT, fill='black')
draw.text((1060, 640), 'kx →', font=BODY_FONT, fill='black')
draw.text((960, 300), 'ky', font=BODY_FONT, fill='black')
img.save(FIG_DIR / 'figure_7_3.png', optimize=True)
path_map['7.3'] = 'figures/figure_7_3.png'
caption_text['7.3'] = 'Building a 2D k-space matrix line by line.'
text_map['7.3'] = [
    '2D MRI is conceptually straightforward.',
    '1. Select a slice. 2. Fill a matrix in k-space. 3. Take the 2D FT.',
    'The k parameter is simply the time-integral of a gradient.',
]

# Figure 8.3: keep the full annotated slide so arrow-linked explanatory tags remain inside the figure.
page_8_3 = DOC[118 - 1]
img = crop_page(118, page_8_3.rect, zoom=2.2)
img.save(FIG_DIR / 'figure_8_3.png', optimize=True)
path_map['8.3'] = 'figures/figure_8_3.png'
caption_text['8.3'] = 'Example of good EPI and corresponding temporal-SNR / standard-deviation images.'
text_map['8.3'] = extract_text_blocks_from_page(118)

# Figure 6.2: keep the pulse-sequence diagram and move the slide title/explanation into prose.
override_figure_with_custom_crops(
    '6.2',
    crop_specs=[
        {'page': 48, 'crop': (0.14, 0.20, 0.84, 0.73)},
    ],
    cols=1,
    text_pages=[48],
    pretitle='Slice selection also needs a refocusing gradient (echo) in practice',
)

# Final source-layout overrides for dense teaching sequences.
override_figure_with_custom_crops(
    '9.1',
    crop_specs=[
        {'page': 90, 'crop': (0.10, 0.21, 0.90, 0.60)},
        {'page': 91, 'crop': (0.05, 0.08, 0.95, 0.92)},
        {'page': 92, 'crop': (0.02, 0.38, 0.97, 0.93)},
    ],
    cols=1,
    chunk_size=1,
    text_pages=[90, 91, 92],
)
override_figure_with_full_pages('9.3', cols=1, pages=[97, 98, 99], chunk_size=1)
override_figure_with_custom_crops(
    '9.4',
    crop_specs=[
        {'page': 103, 'crop': (0.12, 0.30, 0.89, 0.90)},
        {'page': 105, 'crop': (0.02, 0.30, 0.98, 0.94)},
        {'page': 106, 'crop': (0.04, 0.20, 0.96, 0.93)},
    ],
    cols=1,
    chunk_size=1,
    text_pages=[103, 104, 105, 106],
)
override_figure_with_custom_crops(
    '9.5',
    crop_specs=[
        {'page': 108, 'crop': (0.02, 0.38, 0.98, 0.85)},
        {'page': 109, 'crop': (0.18, 0.20, 0.88, 0.91)},
        {'page': 110, 'crop': (0.18, 0.18, 0.82, 0.92)},
    ],
    cols=1,
    chunk_size=1,
    text_pages=[108, 109, 110],
)
override_figure_with_mixed_pages(
    '11.1',
    visual_pages=[141, 144, 147, 148, 151, 157],
    text_pages=[146, 149, 155, 158],
    cols=2,
    chunk_size=2,
)
override_figure_with_mixed_pages(
    '11.2',
    visual_pages=[160, 163, 165, 166],
    text_pages=[164, 167],
    title_pages=[159],
    cols=1,
    chunk_size=1,
)
override_figure_with_custom_crops(
    '11.3',
    crop_specs=[
        {'page': 173, 'crop': (0.06, 0.23, 0.94, 0.80)},
        {'page': 175, 'crop': (0.04, 0.14, 0.96, 0.80)},
        {'page': 176, 'crop': (0.03, 0.28, 0.97, 0.94)},
    ],
    cols=1,
    chunk_size=1,
    text_pages=[169, 170, 173, 175, 176, 177],
    pretitle='Simultaneous multi-slice (SMS) EPI',
    presubtitle='a.k.a. multi-band (MB) EPI',
)
override_figure_with_full_pages('12.3', cols=1, pages=[192, 199], chunk_size=1)
override_figure_with_full_pages('12.5', cols=2, pages=[201, 202, 203, 204, 205, 209, 210, 211, 214], chunk_size=2)
override_figure_with_full_pages('13.1', cols=1, pages=[219, 220, 221, 222, 224], chunk_size=1)
callout_map['11.1'] = normalize_callouts_for_figure('11.1', MANUAL_POSTTEXT['11.1'])
callout_map['11.3'] = normalize_callouts_for_figure('11.3', MANUAL_POSTTEXT['11.3'])
callout_map['13.1'] = []

# Figure 12.6: keep a synthetic troubleshooting sheet, but include the actual drift clues and diagnostic prompts from the source.
img = Image.new('RGB', (1800, 1180), 'white')
draw = ImageDraw.Draw(img)
draw.text((70, 55), 'Figure 12.6. Troubleshooting decision checklist.', font=TITLE_FONT, fill='black')
draw.rounded_rectangle((80, 150, 820, 640), radius=28, outline='black', width=4, fill=(245, 248, 252))
draw.text((120, 190), 'System drifts & chronic motion', font=TITLE_FONT, fill='black')
draw.multiline_text(
    (120, 250),
    '~10 mins is the warning sign.\n\n'
    '- Foam padding?\n'
    '- Talking?\n'
    '- Other systemic or chronic effects?\n\n'
    'Adjust if needed:\n'
    '- Coil sensitivity map\n'
    '- pTx shim\n'
    '- B0 shim',
    font=BODY_FONT,
    fill='black',
    spacing=12,
)
draw.rounded_rectangle((960, 150, 1720, 520), radius=28, outline='black', width=4, fill=(245, 248, 252))
draw.text((1000, 190), 'Tactics for diagnosis', font=TITLE_FONT, fill='black')
draw.multiline_text(
    (1000, 255),
    '1. Assess temporal stability\n'
    '2. Acquire a short retest\n'
    '3. Make a brief list of possible explanations\n'
    '4. Develop a most likely hypothesis',
    font=BODY_FONT,
    fill='black',
    spacing=18,
)
draw.rounded_rectangle((80, 690, 1640, 1035), radius=28, outline='black', width=4, fill=(250, 251, 253))
draw.text((120, 690), 'Questions to test the hypothesis', font=TITLE_FONT, fill='black')
draw.multiline_text(
    (120, 770),
    '- Does the problem exist in a different type of scan?\n'
    '- Can you make the problem worse?\n'
    '- Consider removing the subject and setting up again.\n'
    '- Consider running a short QC test.',
    font=BODY_FONT,
    fill='black',
    spacing=18,
)
draw.text((1040, 1080), 'Test simple explanations first, then escalate.', font=BODY_FONT, fill='black')
img.save(FIG_DIR / 'figure_12_6.png', optimize=True)
path_map['12.6'] = 'figures/figure_12_6.png'
caption_text['12.6'] = 'Troubleshooting decision checklist.'
text_map['12.6'] = [
    'System drifts & chronic motion.',
    'Foam padding? Talking? Other systemic or chronic effects?',
    '~10 mins.',
    'Adjust: coil sensitivity map, pTx shim, B0 shim.',
    'Tactics for diagnosis.',
    'Assess temporal stability.',
    'Acquire a short retest.',
    'Make a brief list of possible explanations.',
    'Develop a most likely hypothesis.',
    'Does the problem exist in a different type of scan?',
    'Can you make the problem worse?',
    'Consider removing subject & setting up again.',
    'Consider running a short QC test.',
]
callout_map['12.6'] = []

# Figure 13.3: synthesize the MRI / auxiliary comparison, but preserve all three source-table themes.
img = Image.new('RGB', (1800, 1180), 'white')
draw = ImageDraw.Draw(img)
draw.text((70, 55), 'Figure 13.3. MRI-based versus auxiliary-data-based confound assessment.', font=TITLE_FONT, fill='black')
draw.rounded_rectangle((90, 170, 820, 610), radius=28, outline='black', width=4, fill=(245, 248, 252))
draw.text((130, 210), 'MRI scans are especially useful when...', font=TITLE_FONT, fill='black')
draw.multiline_text(
    (130, 285),
    '- the confound is mostly spatial or image-space\n'
    '- you need distortion fields or susceptibility structure\n'
    '- you need temporal-stability maps (tSNR / stdev)\n'
    '- TE dependence or multi-echo behavior matters',
    font=BODY_FONT,
    fill='black',
    spacing=16,
)
draw.rounded_rectangle((980, 170, 1710, 610), radius=28, outline='black', width=4, fill=(245, 248, 252))
draw.multiline_text((1020, 205), 'Simultaneous auxiliary data\nare especially useful when...', font=TITLE_FONT, fill='black', spacing=6)
draw.multiline_text(
    (1020, 330),
    '- physiology varies over time during the scan\n'
    '- respiration, pulse, CO2/O2, or eye behavior matter\n'
    '- task compliance or arousal is uncertain\n'
    '- imaging alone cannot disambiguate the nuisance source',
    font=BODY_FONT,
    fill='black',
    spacing=16,
)
draw.rounded_rectangle((250, 690, 1550, 1035), radius=28, outline='black', width=4, fill=(250, 251, 253))
draw.text((290, 730), 'Pre/post-scan data are especially useful when...', font=TITLE_FONT, fill='black')
draw.multiline_text(
    (290, 800),
    '- baseline state or history matters to interpretation\n'
    '- caffeine, sleep, medication, exercise, or anxiety may shift the result\n'
    '- group differences may reflect biologic state, not only acquisition\n'
    '- the study needs documented context before modeling the confounds',
    font=BODY_FONT,
    fill='black',
    spacing=16,
)
draw.multiline_text(
    (360, 1065),
    'Best practice: combine MRI, simultaneous auxiliary data,\n'
    'and pre/post-scan context when the study can afford it.',
    font=BODY_FONT,
    fill='black',
    spacing=10,
)
img.save(FIG_DIR / 'figure_13_3.png', optimize=True)
path_map['13.3'] = 'figures/figure_13_3.png'
caption_text['13.3'] = 'MRI-based versus auxiliary-data-based confound assessment.'
text_map['13.3'] = [
    'Relative utility of MRI scans to capture biological confounds.',
    'Relative utility of simultaneous auxiliary data.',
    'Relative importance of auxiliary data to collect pre/post scan.',
]
callout_map['13.3'] = []

# Synthesized Figures 14.1 and 14.2 remain textbook-style originals.
img = Image.new('RGB', (1800, 900), 'white')
draw = ImageDraw.Draw(img)
boxes = [
    (80, 280, 430, 620, 'Acquisition choices\n\nTE, TR, PE direction,\nresolution, partial Fourier,\nGRAPPA, SMS, multi-echo'),
    (510, 280, 860, 620, 'Artifact burden\n\nGhosting, distortion,\ndropout, residual aliasing,\ninstability, drift'),
    (940, 280, 1290, 620, 'QC findings\n\nMean image, stdev image,\ntSNR, motion traces,\nregion-specific vulnerability'),
    (1370, 280, 1720, 620, 'Interpretive risk\n\nNeural vs non-neural signal,\nregional confidence,\nstudy-specific confounds'),
]
for x1, y1, x2, y2, text in boxes:
    draw.rounded_rectangle((x1, y1, x2, y2), radius=30, outline='black', width=4, fill=(245, 248, 252))
    yy = y1 + 40
    for idx, line in enumerate(text.split('\n')):
        font = TITLE_FONT if idx == 0 else BODY_FONT
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        draw.text((x1 + (x2 - x1 - tw) / 2, yy), line, font=font, fill='black')
        yy += 46 if idx == 0 else 40
for i in range(3):
    x2 = boxes[i][2]
    x1n = boxes[i + 1][0]
    y = 450
    draw.line((x2 + 20, y, x1n - 40, y), fill='black', width=8)
    draw.polygon([(x1n - 40, y), (x1n - 70, y - 18), (x1n - 70, y + 18)], fill='black')
draw.text((90, 80), 'Figure 14.1. Acquisition choices -> artifact burden -> QC findings -> interpretive risk.', font=TITLE_FONT, fill='black')
draw.text((90, 140), 'Synthetic summary figure showing how protocol decisions propagate forward into QC and scientific interpretation.', font=BODY_FONT, fill='black')
img.save(FIG_DIR / 'figure_14_1.png', optimize=True)
path_map['14.1'] = 'figures/figure_14_1.png'
caption_text['14.1'] = 'Integrated concept map from acquisition choice to artifact burden to interpretive risk.'
text_map['14.1'] = []

img = Image.new('RGB', (1800, 1200), 'white')
draw = ImageDraw.Draw(img)
draw.text((70, 60), 'Figure 14.2. Pre-scan, in-scan, and post-scan practical checklist.', font=TITLE_FONT, fill='black')
columns = [
    ('Pre-scan', [
        'Document caffeine, sleep, medication, and relevant state factors.',
        'Confirm task understanding and comfort.',
        'Seat the coil stably and check padding / cables.',
        'Choose PE direction, TE, slice thickness, and acceleration deliberately.',
        'Plan auxiliary recordings if the study needs them.',
    ]),
    ('In-scan', [
        'Compare quickly against known-good EPI.',
        'Look for ghosting, distortion, dropout, spikes, or leakage.',
        'Check whether artifacts overlap the region of interest.',
        'Watch motion, talking, breathing irregularity, and fatigue.',
        'Use a short retest when the cause is uncertain.',
    ]),
    ('Post-scan', [
        'Review mean image, stdev image, tSNR, and motion estimates.',
        'Note unusual subject behavior or scanner-room events.',
        'Assess whether confounds threaten the main interpretation.',
        'Decide whether auxiliary data are adequate for nuisance modeling.',
        'Record follow-up changes for the next session.',
    ]),
]


def wrapped_text(draw_obj, text, font, width_px):
    words = text.split()
    lines = []
    current = ''
    for word in words:
        test = (current + ' ' + word).strip()
        if draw_obj.textlength(test, font=font) <= width_px or not current:
            current = test
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


col_w = 500
x_positions = [70, 650, 1230]
for (title, bullets), x in zip(columns, x_positions):
    draw.rounded_rectangle((x, 180, x + col_w, 1080), radius=26, outline='black', width=4, fill=(245, 248, 252))
    draw.text((x + 30, 220), title, font=TITLE_FONT, fill='black')
    y = 300
    for bullet in bullets:
        draw.ellipse((x + 30, y + 10, x + 44, y + 24), fill='black')
        for line in wrapped_text(draw, bullet, BODY_FONT, col_w - 80):
            draw.text((x + 60, y), line, font=BODY_FONT, fill='black')
            y += 34
        y += 30
img.save(FIG_DIR / 'figure_14_2.png', optimize=True)
path_map['14.2'] = 'figures/figure_14_2.png'
caption_text['14.2'] = 'Pre-scan, in-scan, and post-scan practical checklist.'
text_map['14.2'] = []


# Build polished manuscript with extracted-asset figures, but keep raw source-text extracts out of the textbook body.
text = FULL_MD.read_text(encoding='utf-8')
if text.startswith('?# '):
    text = text[1:]
text = repair_text_surface(text)
text = text.replace('## Textbook Manuscript — Front Matter, Chapters 13–14, and End Matter', '## Full Integrated Manuscript (Extracted-Asset Figure Draft)')
text = text.replace('## Full Integrated Manuscript (Polished Figure-Integrated Draft)', '## Full Integrated Manuscript (Extracted-Asset Figure Draft)')
pattern = re.compile(r'\*\*Figure\s+(\d+\.\d+)\s+\(planned\)\.\*\*\s*(.+)')
new_lines = []
for line in text.splitlines():
    match = pattern.match(line.strip())
    if not match:
        new_lines.append(line)
        continue
    num = match.group(1)
    desc = caption_text.get(num, match.group(2).strip())
    img_rel = path_map.get(num)
    img_rels = img_rel if isinstance(img_rel, list) else ([img_rel] if img_rel else [])
    pretitle = clean_text_block(pretitle_map.get(num, ''))
    presubtitle = clean_text_block(presubtitle_map.get(num, ''))
    if len(re.findall(r'[A-Za-z]', pretitle)) < 4:
        pretitle = ''
    if len(re.findall(r'[A-Za-z]', presubtitle)) < 6:
        presubtitle = ''
    if pretitle:
        new_lines.append(f'**{pretitle}**')
        new_lines.append('')
    if presubtitle:
        new_lines.append(presubtitle)
        new_lines.append('')
    for rel in img_rels:
        new_lines.append(f'![Figure {num}. {desc}]({rel})')
        new_lines.append('')
    new_lines.append(f'**Figure {num}. {desc}**')
    callouts = [normalize_extracted_paragraph(x) for x in callout_map.get(num, [])]
    callouts = [x for x in callouts if x]
    if callouts:
        new_lines.append('')
        for callout in callouts:
            new_lines.append(callout)
            new_lines.append('')
    else:
        new_lines.append('')
POLISHED_MD.write_text('\n'.join(new_lines) + '\n', encoding='utf-8')


with MANIFEST.open('w', encoding='utf-8') as handle:
    handle.write('# Figure Manifest\n\n')
    for num in sorted(path_map.keys(), key=lambda s: [int(x) for x in s.split('.')]):
        pages = page_map.get(num, [])
        paths = path_map[num] if isinstance(path_map[num], list) else [path_map[num]]
        handle.write(f'- Figure {num}: `{paths[0]}`\n')
        for extra_path in paths[1:]:
            handle.write(f'  - Continued image: `{extra_path}`\n')
        handle.write(f'  - Caption: {caption_text[num]}\n')
        if pages:
            handle.write(f'  - Source pages: {", ".join(str(p) for p in pages)}\n')
        handle.write('\n')

with TEXT_EXTRACTS.open('w', encoding='utf-8') as handle:
    handle.write('# Figure Source Text Extracts\n\n')
    for num in sorted(text_map.keys(), key=lambda s: [int(x) for x in s.split('.')]):
        pages = page_map.get(num, [])
        handle.write(f'## Figure {num}\n\n')
        handle.write(f'- Caption: {caption_text[num]}\n')
        if pages:
            handle.write(f'- Source pages: {", ".join(str(p) for p in pages)}\n')
        lines = text_map.get(num, [])
        if lines:
            handle.write('- Extracted text:\n')
            for line in lines:
                handle.write(f'  - {line}\n')
        else:
            handle.write('- Extracted text: none (synthetic textbook figure).\n')
        handle.write('\n')

print(POLISHED_MD)
print(MANIFEST)
print(TEXT_EXTRACTS)
print(f'figure_count={len(path_map)}')
