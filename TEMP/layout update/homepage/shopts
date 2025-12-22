// src/types/shop.ts - ENHANCED VERSION

export interface Product {
  id: string;
  name: string;
  price: string;
  slug?: string;  // ← ADD THIS LINE
  originalPrice: string;
  image: string;
  imageAlt?: string;
  affiliateUrl: string;
  category: string;
  isNew?: boolean;
  isTrending?: boolean;
  rating?: number;
  reviewCount?: number;
  description?: string;
  cta: string;
  stockStatus?: 'in-stock' | 'low-stock' | 'out-of-stock';
  brand?: string;
  sku?: string;
}

// 🆕 NEW: Extended product interface for individual product pages
export interface ProductPageData extends Product {
  slug: string; // URL-friendly version of name
  seo: {
    title: string;
    description: string;
    keywords: string[];
    ogImage: string;
  };
  
  // Rich 400-word description
  fullDescription: {
    html: string;
    plainText: string;
  };
  
  // Product specifications
  specifications?: {
    packageContents?: string;
    material?: string;
    finish?: string;
    durability?: string;
    applicationTime?: string;
    reusable?: string;
    sizes?: string;
  };
  
  // Related content for internal linking
  relatedProducts: string[]; // Array of product IDs
  relatedCategories: string[]; // Array of category slugs
  
  internalLinks: {
    blog?: {
      title: string;
      slug: string;
      image: string;
      excerpt?: string;
    };
    inspo?: {
      title: string;
      slug: string;
      image: string;
      category?: string;
    };
    topic?: {
      title: string;
      slug: string;
      image: string;
      description?: string;
    };
  };
  
  // FAQs for this specific product
  faqs?: Array<{
    question: string;
    answer: string;
  }>;
}

export interface CategorySEO {
  title: string;
  description: string;
  keywords: string;
  ogImage: string;
}

export interface HeroSection {
  title: string;
  subtitle: string;
  image: string;
  gradient: string;
  floatingEmojis: string[];
}

export interface RelatedCategory {
  name: string;
  slug: string;
  image: string;
}

export interface FAQ {
  question: string;
  answer: string;
  keywords?: string[];
}

export interface FAQData {
  category: string;
  faqs: FAQ[];
}

export interface CategoryDescription {
  category: string;
  html: string;
  perfectFor?: string[];
}

export interface CategoryRating {
  rating: number;
  reviews: number;
}

export interface CategoryData {
  slug: string;
  displayName: string;
  season: string;
  year: number;
  description: string;
  heroImage: string;
  gradientFrom: string;
  gradientVia: string;
  gradientTo: string;
  emojis: string[];
  ctas: string[];
  seo: CategorySEO;
  relatedCategories: string[];
  whyChooseUs?: string[];
  tldr?: {
    summary: string[];
    keyTakeaways?: string[];
  };
}

export interface CompleteCategoryData extends CategoryData {
  faqs?: FAQ[];
  categoryDescription?: CategoryDescription;
  rating?: CategoryRating;
  productCount?: number;
  priceRange?: {
    min: number;
    max: number;
  };
}

export interface CategoriesData {
  categories: {
    [slug: string]: CategoryData;
  };
}

export interface ProductsData {
  products: Product[];
}

// 🆕 NEW: Product page data structure
export interface ProductPageDataCollection {
  category: string;
  totalProducts: number;
  products: {
    [id: string]: ProductPageData;
  };
}
