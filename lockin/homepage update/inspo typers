// src/types/inspo.ts
// Types for nail design inspiration pages

export interface DesignImage {
  id: string;
  url: string;
  alt: string;
  category?: string;
  isPremium?: boolean;
  pinterestUrl?: string;
}

export interface DesignSEO {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
}

export interface HeroSection {
  title: string;
  subtitle: string;
  image: string;
  gradient: string;
  floatingEmojis: string[];
}

export interface FAQ {
  question: string;
  answer: string;
  keywords?: string[];
}

export interface DesignData {
  slug: string;
  displayName: string;
  category: string; // e.g., "Classic", "Trendy", "Seasonal"
  year: number;
  description: string;
  heroImage: string;
  gradientFrom: string;
  gradientVia: string;
  gradientTo: string;
  emojis: string[];
  ctas: string[];
  tldr?: {
    summary: string[];
    keyTakeaways?: string[];
  };
  seo: DesignSEO;
  relatedDesigns: string[];
  perfectFor?: string[];
  styleGuide?: string[];
}

export interface CompleteDesignData extends DesignData {
  faqs?: FAQ[];
  images?: DesignImage[];
  designDescription?: {
    category: string;
    html: string;
    perfectFor?: string[];
  };
  imageCount?: number;
}

export interface DesignsData {
  designs: {
    [slug: string]: DesignData;
  };
}

export interface ImagesData {
  images: DesignImage[];
}
