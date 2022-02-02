const config = {
	content: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		extend: {
			maxHeight: {
				'detail': 'calc(100vh - 2.5rem)',
			},
		}
	},

	plugins: []
};

module.exports = config;
