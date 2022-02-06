<script>
	import '../app.css';
	import Nav from '$lib/components/Nav.svelte';

	import {createClient, setClient} from '@urql/svelte'

	const client = createClient({
		url:'http://localhost:8000/api/',
		fetchOptions:() => {
			return {mode: 'no-cors', referrerPolicy:'same-origin'}
		}
	})

	setClient(client)
</script>

<Nav/>
<slot />
