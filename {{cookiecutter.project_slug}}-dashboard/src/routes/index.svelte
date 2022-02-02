<script>
import Stats from '$lib/components/dashboard/stats.svelte';
import Nav from '$lib/components/Nav.svelte';
import ListView from '$lib/components/orders/ListView.svelte';
</script>
<div class="min-h-full">
    <div class="bg-gray-800 pb-32">
        <Nav />
      <header class="py-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 class="text-3xl font-bold text-white">
            Dashboard
          </h1>
        </div>
      </header>
    </div>
  
    <main class="-mt-32">
      <div class="max-w-7xl mx-auto pb-12 px-4 sm:px-6 lg:px-8">
        <Stats />
      </div>
    </main>

    <div class="max-w-7xl mx-auto pb-12 px-4 sm:px-6 lg:px-8">
        <ListView />
    </div>
  </div>
  <div class="h-screen"></div>
  