import type { CategoryData, Product, CategoriesData, ProductsData } from '@/types/shop';
import categoriesData from '@/content/shop-categories.json';

/**
 * Get category metadata by slug
 */
export function getCategoryData(slug: string): CategoryData | null {
  const data = categoriesData as any;
  const category = data.categories?.[slug];
  
  if (!category) return null;
  
  if (category.seo && typeof category.seo.keywords === 'string') {
    category.seo.keywords = category.seo.keywords.split(',').map((k: string) => k.trim());
  }
  
  return category as CategoryData;
}

/**
 * Get all products for a specific category
 */
export async function getCategoryProducts(slug: string): Promise<Product[]> {
  try {
    const productsData = await import(`@/content/shop-products/${slug}.json`) as any;
    
    // Convert object to array
    if (productsData.products && typeof productsData.products === 'object') {
      return Object.values(productsData.products);
    }
    
    return productsData.products || [];
  } catch (error) {
    console.error(`Error loading products for category: ${slug}`, error);
    return [];
  }
}
/**
 * Get all category slugs for static generation
 */
export function getAllCategorySlugs(): string[] {
  const data = categoriesData as CategoriesData;
  return Object.keys(data.categories);
}

/**
 * Get related categories with their metadata
 */
export function getRelatedCategories(slug: string, limit: number = 3): CategoryData[] {
  const currentCategory = getCategoryData(slug);
  if (!currentCategory) return [];

  const relatedSlugs = currentCategory.relatedCategories.slice(0, limit);
  const relatedCategories: CategoryData[] = [];

  for (const relatedSlug of relatedSlugs) {
    const category = getCategoryData(relatedSlug);
    if (category) {
      relatedCategories.push(category);
    }
  }

  return relatedCategories;
}

/**
 * Get total product count for a category
 */
export async function getCategoryProductCount(slug: string): Promise<number> {
  const products = await getCategoryProducts(slug);
  return products.length;
}

/**
 * Filter products by type
 */
export function filterProducts(products: Product[], filter: 'all' | 'new' | 'trending' | 'sale'): Product[] {
  switch (filter) {
    case 'new':
      return products.filter(p => p.isNew);
    case 'trending':
      return products.filter(p => p.isTrending);
    case 'sale':
      return products.filter(p => p.originalPrice !== p.price);
    case 'all':
    default:
      return products;
  }
}

/**
 * Calculate discount percentage from string prices
 */
export function calculateDiscount(originalPrice: string, currentPrice: string): number {
  const original = parseFloat(originalPrice.replace('$', ''));
  const current = parseFloat(currentPrice.replace('$', ''));
  
  if (original === 0 || current >= original) return 0;
  
  return Math.round(((original - current) / original) * 100);
}

/**
 * Get 15 random products from all categories for showcase
 * Returns mixed products (2-3 from each category)
 */
export async function getShowcaseProducts(): Promise<Product[]> {
  const categorySlugs = getAllCategorySlugs();
  const showcaseProducts: Product[] = [];
  
  // Number of products to pick from each category
  const productsPerCategory = Math.ceil(15 / categorySlugs.length);
  
  for (const slug of categorySlugs) {
    try {
      const products = await getCategoryProducts(slug);
      
      // Shuffle and pick random products
      const shuffled = products.sort(() => 0.5 - Math.random());
      const selected = shuffled.slice(0, productsPerCategory);
      
      showcaseProducts.push(...selected);
    } catch (error) {
      console.error(`Error loading showcase products for ${slug}:`, error);
    }
  }
  
  // Shuffle final array and limit to exactly 15
  const finalShowcase = showcaseProducts
    .sort(() => 0.5 - Math.random())
    .slice(0, 15);
  
  return finalShowcase;
}
