import cv2, sys
import numpy as np


def sumsq(x):
    return np.sum(np.square(x))


def RMSE(f, g):
    return np.sqrt(sumsq(f - g) / f.size)

def SNR(f, g):
    return 10 * np.log10(sumsq(f) / sumsq(f - g))

def PSNR(f, g):
    return 20 * np.log10(255 / RMSE(f, g))

def cov(f, g):
    mf, mg = np.mean(f), np.mean(g)
    return np.sum((f - mf) * (g - mg)) / f.size

def corr(f, g):
    mf, mg = np.mean(f), np.mean(g)
    return np.sum((f - mf) * (g - mg)) / np.sqrt(sumsq(f - mf) * sumsq(g - mg))

def jaccard(f, g):
    return np.count_nonzero(f == g) / f.size


DIFS = [RMSE, SNR, PSNR, corr, cov, jaccard]

varredura = 'alternada'

_, idx = sys.argv



DISTS = [
    'Floyd e Steinberg',
    'Stevenson e Arci',
    'Burkes',
    'Sierra',
    'Stucki',
    'Jarvis, Judice e Ninke'
]
distr = DISTS[int(idx)]
dist = distr.split(' ')[0].rstrip(',').lower()

print('\\multirow{6}{*}{' + distr + '}')

for img in ['baboon', 'peppers', 'monalisa', 'watch']:

    f = cv2.imread(f'imagens/{img}.png')
    g = cv2.imread(f'build/{varredura}/{dist}/{img}.png')

    if f is None or g is None:
        raise ValueError(f'não foi possível ler imagens', (img, dist, varredura))

    print(f'& \\texttt{{{img}.png}} &', ' & '.join(f'{fn(f, g):.3f}' for fn in [RMSE, SNR, PSNR, corr]), '\\\\')

print('\\midrule')

# for fun in DIFS:
#     name = fun.__name__
#     print(f'\t{name:>8s} {fun(f, g):9.3f}')
