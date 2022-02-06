<script>
    import '../../app.css'
    import Nav from '$lib/components/admin/AdminNav.svelte'
import { append } from 'svelte/internal';
</script>

<!-- <Nav /> -->
<div class="min-h-full">
    <div class="bg-gray-800 pb-32">
        <Nav />
      <header class="py-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 class="text-3xl font-bold text-white">
            Admin dashboard
          </h1>
        </div>
      </header>
    </div>
  
    <slot />
  <div class="h-screen"></div>
</div>