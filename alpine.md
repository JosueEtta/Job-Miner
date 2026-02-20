# Archive Project Modal: Component Documentation

This component is a responsive confirmation dialog built with **Alpine.js** and **Tailwind CSS**. It is designed to be accessible, performant, and easy to customize for any "Action Confirmation" workflow.

---

## ## 1. Technical Stack
* **Logic:** [Alpine.js](https://alpinejs.dev/) (Lightweight JavaScript framework)
* **Styling:** [Tailwind CSS](https://tailwindcss.com/) (Utility-first CSS)
* **Icons:** [Heroicons](https://heroicons.com/) (SVG-based)

---

## ## 2. Core Features
| Feature | Description |
| :--- | :--- |
| **Stateful** | Uses `x-data` to manage "Open/Closed" states without external JS files. |
| **Animated** | Features smooth scale and opacity transitions via `x-transition`. |
| **Responsive** | Automatically adjusts layout for mobile (bottom-aligned) and desktop (centered). |
| **Dark Mode** | Full support for dark themes using Tailwind's `dark:` variant. |
| **Accessible** | Implements `aria-modal`, `role="dialog"`, and focus management basics. |

---

## ## 3. Installation & Setup

### ### A. CDN Method (Fastest)
Add these scripts to the `<head>` of your HTML file to enable the functionality:

```html
<script defer src="[https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js](https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js)"></script>
<script src="[https://cdn.tailwindcss.com](https://cdn.tailwindcss.com)"></script>