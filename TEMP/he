'use client';
import { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';

const BLOG_LINKS = [
  { label: 'Christmas Nails', href: '/blog/christmas-nail-designs-2025' },
  { label: 'Seasonal Nails Ideas', href: '/topics/seasonal-trends' },
  { label: 'Nail Art Guide 2025', href: '/topics/nail-art-guides' },
  { label: 'Professional Women', href: '/topics/modern-women' },
  { label: 'Browse All Topics', href: '/topics' },
];

const SHOP_LINKS = [
  { label: 'Christmas Nails', href: '/shop/christmas' },
  { label: 'Winter Designs', href: '/shop/winter' },
  { label: 'Halloween Styles', href: '/shop/halloween' },
  { label: 'Trendy Collections', href: '/shop/trendy' },
  { label: 'View All Collections', href: '/shop' },
];

const DESIGNS_LINKS = [
  { label: 'Chrome Metallic Winter Nails', href: '/inspo/chrome-metallic-winter-nails' },
  { label: 'Burgundy Wine Winter Nails', href: '/inspo/burgundy-wine-winter-nails' },
  { label: 'Chocolate Brown Winter Nails', href: '/inspo/chocolate-brown-winter-nails' },
  { label: 'Velvet Cat Eye Winter Nails', href: '/inspo/velvet-cat-eye-winter-nails' },
  { label: 'View All Collections', href: '/inspo' },
];

const TOPICS_LINKS = [
  { label: 'Seasonal Trends', href: '/topics/seasonal-trends' },
  { label: 'Nail Art Guides', href: '/topics/nail-art-guides' },
  { label: 'Modern Women', href: '/topics/modern-women' },
  { label: 'Beauty Tips', href: '/topics/beauty-tips' },
  { label: 'Browse All Topics', href: '/topics' },
];

export default function Header() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [mobileDropdowns, setMobileDropdowns] = useState({
    blog: false,
    shop: false,
    designs: false,
    topics: false,
  });

  const toggleMobileDropdown = (key: 'blog' | 'shop' | 'designs' | 'topics') => {
    setMobileDropdowns(prev => ({ ...prev, [key]: !prev[key] }));
  };

  return (
    <header className="sticky top-0 z-50 bg-accent">
      {/* Top Bar */}
      <div className="border-b border-text-primary/20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-end items-center h-10 gap-8">
            <Link 
              href="/newsletter" 
              className="text-xs tracking-widest uppercase text-text-primary hover:text-surface transition-colors duration-300 relative group"
            >
              Newsletter
              <span className="absolute bottom-0 left-0 w-0 h-[1px] bg-text-primary group-hover:w-full transition-all duration-500 ease-out"></span>
            </Link>
            <Link 
              href="/work-with-us" 
              className="text-xs tracking-widest uppercase text-text-primary hover:text-surface transition-colors duration-300 relative group"
            >
              Collaborate
              <span className="absolute bottom-0 left-0 w-0 h-[1px] bg-text-primary group-hover:w-full transition-all duration-500 ease-out"></span>
            </Link>
          </div>
        </div>
      </div>

      {/* Main Navigation */}
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-20">
          
          {/* Left Navigation */}
          <div className="hidden md:flex items-center space-x-8 flex-1">
            <Link 
              href="/" 
              className="text-sm tracking-wider uppercase text-text-primary hover:text-accent transition-colors duration-300 relative group font-medium"
            >
              Home
              <span className="absolute bottom-0 left-0 w-0 h-[1px] bg-text-primary group-hover:w-full transition-all duration-500 ease-out"></span>
            </Link>

            <Link 
              href="/about" 
              className="text-sm tracking-wider uppercase text-text-primary hover:text-accent transition-colors duration-300 relative group font-medium"
            >
              About
              <span className="absolute bottom-0 left-0 w-0 h-[1px] bg-text-primary group-hover:w-full transition-all duration-500 ease-out"></span>
            </Link>

            {/* Blog Dropdown */}
            <div className="relative group">
              <button className="text-sm tracking-wider uppercase text-text-primary hover:text-accent transition-colors duration-300 font-medium flex items-center gap-1 relative">
                Blog
                <svg className="w-3 h-3 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
                <span className="absolute bottom-0 left-0 w-0 h-[1px] bg-text-primary group-hover:w-full transition-all duration-500 ease-out"></span>
              </button>
              {/* Dropdown */}
              <div className="fixed left-0 right-0 top-[120px] opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out delay-150 z-50">
                <div className="bg-accent/98 backdrop-blur-sm border-b border-text-primary/20 shadow-2xl">
                  <div className="max-w-7xl mx-auto px-8 py-12">
                    <div className="space-y-1">
                      {BLOG_LINKS.map((link) => (
                        <Link
                          key={link.href}
                          href={link.href}
                          className="block py-3 text-lg text-text-primary hover:text-surface hover:pl-2 transition-all duration-300 relative group/item"
                        >
                          {link.label}
                          <span className="absolute bottom-2 left-0 w-0 h-[1px] bg-surface group-hover/item:w-12 transition-all duration-400"></span>
                        </Link>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Shop Dropdown */}
            <div className="relative group">
              <button className="text-sm tracking-wider uppercase text-text-primary hover:text-accent transition-colors duration-300 font-medium flex items-center gap-1 relative">
                Shop
                <svg className="w-3 h-3 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
                <span className="absolute bottom-0 left-0 w-0 h-[1px] bg-text-primary group-hover:w-full transition-all duration-500 ease-out"></span>
              </button>
              {/* Dropdown */}
              <div className="fixed left-0 right-0 top-[120px] opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out delay-150 z-50">
                <div className="bg-accent/98 backdrop-blur-sm border-b border-text-primary/20 shadow-2xl">
                  <div className="max-w-7xl mx-auto px-8 py-12">
                    <div className="space-y-1">
                      {SHOP_LINKS.map((link) => (
                        <Link
                          key={link.href}
                          href={link.href}
                          className="block py-3 text-lg text-text-primary hover:text-surface hover:pl-2 transition-all duration-300 relative group/item"
                        >
                          {link.label}
                          <span className="absolute bottom-2 left-0 w-0 h-[1px] bg-surface group-hover/item:w-12 transition-all duration-400"></span>
                        </Link>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Designs Dropdown */}
            <div className="relative group">
              <button className="text-sm tracking-wider uppercase text-text-primary hover:text-accent transition-colors duration-300 font-medium flex items-center gap-1 relative">
                Designs
                <svg className="w-3 h-3 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
                <span className="absolute bottom-0 left-0 w-0 h-[1px] bg-text-primary group-hover:w-full transition-all duration-500 ease-out"></span>
              </button>
              {/* Dropdown */}
              <div className="fixed left-0 right-0 top-[120px] opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out delay-150 z-50">
                <div className="bg-accent/98 backdrop-blur-sm border-b border-text-primary/20 shadow-2xl">
                  <div className="max-w-7xl mx-auto px-8 py-12">
                    <div className="space-y-1">
                      {DESIGNS_LINKS.map((link) => (
                        <Link
                          key={link.href}
                          href={link.href}
                          className="block py-3 text-lg text-text-primary hover:text-surface hover:pl-2 transition-all duration-300 relative group/item"
                        >
                          {link.label}
                          <span className="absolute bottom-2 left-0 w-0 h-[1px] bg-surface group-hover/item:w-12 transition-all duration-400"></span>
                        </Link>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Topics Dropdown */}
            <div className="relative group">
              <button className="text-sm tracking-wider uppercase text-text-primary hover:text-accent transition-colors duration-300 font-medium flex items-center gap-1 relative">
                Topics
                <svg className="w-3 h-3 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
                <span className="absolute bottom-0 left-0 w-0 h-[1px] bg-text-primary group-hover:w-full transition-all duration-500 ease-out"></span>
              </button>
              {/* Dropdown */}
              <div className="fixed left-0 right-0 top-[120px] opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out delay-150 z-50">
                <div className="bg-accent/98 backdrop-blur-sm border-b border-text-primary/20 shadow-2xl">
                  <div className="max-w-7xl mx-auto px-8 py-12">
                    <div className="space-y-1">
                      {TOPICS_LINKS.map((link) => (
                        <Link
                          key={link.href}
                          href={link.href}
                          className="block py-3 text-lg text-text-primary hover:text-surface hover:pl-2 transition-all duration-300 relative group/item"
                        >
                          {link.label}
                          <span className="absolute bottom-2 left-0 w-0 h-[1px] bg-surface group-hover/item:w-12 transition-all duration-400"></span>
                        </Link>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Logo - Center */}
          <Link href="/" className="flex items-center space-x-2 group absolute left-1/2 transform -translate-x-1/2 z-10">
            <Image 
              src="/logo.png" 
              alt="Mirelle Inspo" 
              width={48} 
              height={48}
              priority={true}
              className="w-auto h-12 transition-transform duration-300 group-hover:scale-105"
            />
            <span className="font-serif text-2xl font-bold text-text-primary">
              Mirellé
            </span>
          </Link>

          {/* Right Navigation */}
          <div className="hidden md:flex items-center space-x-8 flex-1 justify-end">
            <Link 
              href="/work-with-us" 
              className="text-sm tracking-wider uppercase text-text-primary hover:text-accent transition-colors duration-300 relative group font-medium"
            >
              Work With Us
              <span className="absolute bottom-0 left-0 w-0 h-[1px] bg-text-primary group-hover:w-full transition-all duration-500 ease-out"></span>
            </Link>
          </div>

          {/* Mobile menu button */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="md:hidden text-text-primary relative z-20"
            aria-label="Toggle menu"
          >
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              {mobileMenuOpen ? (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              ) : (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              )}
            </svg>
          </button>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden py-4 space-y-3 border-t border-text-primary/20">
            <Link href="/" className="block text-text-primary hover:text-surface transition-colors font-medium">
              Home
            </Link>
            <Link href="/about" className="block text-text-primary hover:text-surface transition-colors font-medium">
              About
            </Link>

            {/* Blog Accordion */}
            <div>
              <button
                onClick={() => toggleMobileDropdown('blog')}
                className="w-full flex items-center justify-between text-text-primary hover:text-surface transition-colors font-medium"
              >
                Blog
                <svg className={`w-4 h-4 transition-transform duration-300 ${mobileDropdowns.blog ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div className={`overflow-hidden transition-all duration-500 ease-out ${mobileDropdowns.blog ? 'max-h-96 mt-2 opacity-100' : 'max-h-0 opacity-0'}`}>
                <div className="ml-4 space-y-2">
                  {BLOG_LINKS.map((link) => (
                    <Link key={link.href} href={link.href} className="block text-text-primary/80 hover:text-surface transition-colors text-sm">
                      {link.label}
                    </Link>
                  ))}
                </div>
              </div>
            </div>

            {/* Shop Accordion */}
            <div>
              <button
                onClick={() => toggleMobileDropdown('shop')}
                className="w-full flex items-center justify-between text-text-primary hover:text-surface transition-colors font-medium"
              >
                Shop
                <svg className={`w-4 h-4 transition-transform duration-300 ${mobileDropdowns.shop ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div className={`overflow-hidden transition-all duration-500 ease-out ${mobileDropdowns.shop ? 'max-h-96 mt-2 opacity-100' : 'max-h-0 opacity-0'}`}>
                <div className="ml-4 space-y-2">
                  {SHOP_LINKS.map((link) => (
                    <Link key={link.href} href={link.href} className="block text-text-primary/80 hover:text-surface transition-colors text-sm">
                      {link.label}
                    </Link>
                  ))}
                </div>
              </div>
            </div>

            {/* Designs Accordion */}
            <div>
              <button
                onClick={() => toggleMobileDropdown('designs')}
                className="w-full flex items-center justify-between text-text-primary hover:text-surface transition-colors font-medium"
              >
                Designs
                <svg className={`w-4 h-4 transition-transform duration-300 ${mobileDropdowns.designs ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div className={`overflow-hidden transition-all duration-500 ease-out ${mobileDropdowns.designs ? 'max-h-96 mt-2 opacity-100' : 'max-h-0 opacity-0'}`}>
                <div className="ml-4 space-y-2">
                  {DESIGNS_LINKS.map((link) => (
                    <Link key={link.href} href={link.href} className="block text-text-primary/80 hover:text-surface transition-colors text-sm">
                      {link.label}
                    </Link>
                  ))}
                </div>
              </div>
            </div>

            {/* Topics Accordion */}
            <div>
              <button
                onClick={() => toggleMobileDropdown('topics')}
                className="w-full flex items-center justify-between text-text-primary hover:text-surface transition-colors font-medium"
              >
                Topics
                <svg className={`w-4 h-4 transition-transform duration-300 ${mobileDropdowns.topics ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div className={`overflow-hidden transition-all duration-500 ease-out ${mobileDropdowns.topics ? 'max-h-96 mt-2 opacity-100' : 'max-h-0 opacity-0'}`}>
                <div className="ml-4 space-y-2">
                  {TOPICS_LINKS.map((link) => (
                    <Link key={link.href} href={link.href} className="block text-text-primary/80 hover:text-surface transition-colors text-sm">
                      {link.label}
                    </Link>
                  ))}
                </div>
              </div>
            </div>

            <Link href="/work-with-us" className="block text-text-primary hover:text-surface transition-colors font-medium">
              Work With Us
            </Link>
          </div>
        )}
      </nav>
    </header>
  );
}
