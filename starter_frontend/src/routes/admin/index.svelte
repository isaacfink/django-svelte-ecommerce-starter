<script>
import Stats from '$lib/components/admin/stats.svelte';
import Nav from '$lib/components/admin/AdminNav.svelte';
import ListView from '$lib/components/orders/ListView.svelte';
</script>

<main class="-mt-32">
  <div class="max-w-7xl mx-auto pb-12 px-4 sm:px-6 lg:px-8">
    <Stats />
  </div>
</main>

<div class="max-w-7xl mx-auto pb-12 px-4 sm:px-6 lg:px-8">
    <ListView />
</div>
  