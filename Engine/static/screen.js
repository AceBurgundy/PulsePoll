/**
 * Automatically resizes a textarea element to fit its content.
 * @param {HTMLTextAreaElement} textArea - The text area textArea to be resized
 */
export function autoResize(textArea) {
	textArea.style.height = 'auto';
	textArea.style.height = textArea.scrollHeight + 'px';
};

/**
 * returns the current orientation of the device
 *
 * @return {string} 'portrait' or 'landscape'
 */
export function getCurrentOrientation() {
  const PORTRAIT = '(orientation: portrait)';
	const isPortrait = window.matchMedia(PORTRAIT).matches;

  return isPortrait ? 'portrait' : 'landscape';
};
