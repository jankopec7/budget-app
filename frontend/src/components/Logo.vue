<!-- frontend/src/components/Logo.vue -->
<template>
  <svg
    width="180"
    height="50"
    viewBox="0 0 180 50"
    xmlns="http://www.w3.org/2000/svg"
    role="img"
    aria-label="Fintracker logo"
  >
    <rect
      x="1"
      y="1"
      width="178"
      height="48"
      rx="12"
      ry="12"
      fill="#a5d6a7"
      stroke="#2e7d32"
      stroke-width="3"
    />
    <text
      x="50%"
      y="50%"
      dominant-baseline="middle"
      text-anchor="middle"
      fill="#2e7d32"
      font-family="Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
      font-weight="700"
      font-size="24"
    >
      Fintracker
    </text>
  </svg>
</template>

<script>
export default {
  name: "Logo",
};
</script>
