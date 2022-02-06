const config = {
	content: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		extend: {
			maxHeight: {
				'detail': 'calc(100vh - 2.5rem)',
			},
		}
	},

	plugins: [
		require('@tailwindcss/forms'),
		require('@tailwindcss/aspect-ratio'),
		require('@tailwindcss/typography'),
	]
};

module.exports = config;
