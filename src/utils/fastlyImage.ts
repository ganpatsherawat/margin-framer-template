export interface ImageTransformOptions {
  width?: number;
  height?: number;
  fit?: 'bounds' | 'cover' | 'crop';
  quality?: number;
  dpr?: number;
  format?: 'auto' | 'webp' | 'avif' | 'jpeg' | 'png' | 'pjpg';
}

/**
 * Builds an optimized Fastly Image Optimizer URL with transformation query parameters.
 * If the source is an external URL or an SVG, it returns the URL unchanged.
 */
export function getOptimizedImageUrl(
  src: string,
  options: ImageTransformOptions = {}
): string {
  if (!src || src.startsWith('http://') || src.startsWith('https://') || src.endsWith('.svg')) {
    return src;
  }

  const {
    width,
    height,
    fit = 'cover',
    quality = 85,
    dpr = 1,
    format = 'auto'
  } = options;

  const params = new URLSearchParams();
  if (width) params.set('width', width.toString());
  if (height) params.set('height', height.toString());
  if (width && height) params.set('fit', fit);
  if (quality && quality !== 85) params.set('quality', quality.toString());
  if (dpr && dpr > 1) params.set('dpr', dpr.toString());
  if (format && format !== 'auto') params.set('format', format);

  const queryString = params.toString();
  return queryString ? `${src}?${queryString}` : src;
}

/**
 * Builds a standard responsive srcset attribute string.
 */
export function buildSrcSet(
  src: string,
  widths: number[] = [390, 768, 956, 1440],
  options: Omit<ImageTransformOptions, 'width'> = {}
): string {
  if (!src || src.startsWith('http://') || src.startsWith('https://') || src.endsWith('.svg')) {
    return src;
  }

  return widths
    .map((w) => `${getOptimizedImageUrl(src, { ...options, width: w })} ${w}w`)
    .join(', ');
}
