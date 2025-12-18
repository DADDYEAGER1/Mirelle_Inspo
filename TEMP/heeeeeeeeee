'use client';
import { useState } from 'react';
import Link from 'next/link';

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
    <header className="bg-text-primary">
      {/* Top Bar */}
      <div className="border-b border-background/20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-center items-center h-12 relative">
            {/* Logo/Brand - Centered */}
            <Link href="/" className="flex items-center group">
              <span className="font-serif text-2xl font-bold text-background">
                Mirellé
              </span>
            </Link>

            {/* Right Links - Absolute positioned */}
            <div className="flex items-center gap-6 absolute right-0">
              <a 
                href="https://mirelleinspo.com/subscribe" 
                className="text-xs tracking-widest uppercase text-background hover:text-background/70 transition-colors duration-300 border border-background px-3 py-1.5"
              >
                Newsletter
              </a>
              <Link 
                href="/work-with-us" 
                className="text-xs tracking-widest uppercase text-background hover:text-background/70 transition-colors duration-300"
              >
                Work With Us
              </Link>
              <button className="text-background hover:text-background/70 transition-colors">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Main Navigation */}
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-center items-center h-12">
          
          {/* Center Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            <Link 
              href="/" 
              className="text-sm tracking-wider uppercase text-background hover:text-background/70 transition-colors duration-300 font-medium"
            >
              Home
            </Link>

            <Link 
              href="/about" 
              className="text-sm tracking-wider uppercase text-background hover:text-background/70 transition-colors duration-300 font-medium"
            >
              About
            </Link>

            {/* Blog Dropdown */}
            <div className="relative group">
              <button className="text-sm tracking-wider uppercase text-background hover:text-background/70 transition-colors duration-300 font-medium flex items-center gap-1">
                Blog
                <svg className="w-3 h-3 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              {/* Dropdown */}
              <div className="fixed left-0 right-0 top-24 opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out delay-150 z-50">
                <div className="bg-text-primary border-b border-background/20 shadow-2xl" style={{backdropFilter: 'none'}}>
                  <div className="max-w-7xl mx-auto px-8 py-12">
                    <div className="space-y-1">
                      {BLOG_LINKS.map((link) => (
                        <Link
                          key={link.href}
                          href={link.href}
                          className="block py-3 text-lg text-background hover:text-background/70 hover:pl-2 transition-all duration-300"
                        >
                          {link.label}
                        </Link>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Shop Dropdown */}
            <div className="relative group">
              <button className="text-sm tracking-wider uppercase text-background hover:text-background/70 transition-colors duration-300 font-medium flex items-center gap-1">
                Shop
                <svg className="w-3 h-3 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              {/* Dropdown */}
              <div className="fixed left-0 right-0 top-24 opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out delay-150 z-50">
                <div className="bg-text-primary border-b border-background/20 shadow-2xl" style={{backdropFilter: 'none'}}>
                  <div className="max-w-7xl mx-auto px-8 py-12">
                    <div className="space-y-1">
                      {SHOP_LINKS.map((link) => (
                        <Link
                          key={link.href}
                          href={link.href}
                          className="block py-3 text-lg text-background hover:text-background/70 hover:pl-2 transition-all duration-300"
                        >
                          {link.label}
                        </Link>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Designs Dropdown */}
            <div className="relative group">
              <button className="text-sm tracking-wider uppercase text-background hover:text-background/70 transition-colors duration-300 font-medium flex items-center gap-1">
                Designs
                <svg className="w-3 h-3 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              {/* Dropdown */}
              <div className="fixed left-0 right-0 top-24 opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out delay-150 z-50">
                <div className="bg-text-primary border-b border-background/20 shadow-2xl" style={{backdropFilter: 'none'}}>
                  <div className="max-w-7xl mx-auto px-8 py-12">
                    <div className="space-y-1">
                      {DESIGNS_LINKS.map((link) => (
                        <Link
                          key={link.href}
                          href={link.href}
                          className="block py-3 text-lg text-background hover:text-background/70 hover:pl-2 transition-all duration-300"
                        >
                          {link.label}
                        </Link>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Topics Dropdown */}
            <div className="relative group">
              <button className="text-sm tracking-wider uppercase text-background hover:text-background/70 transition-colors duration-300 font-medium flex items-center gap-1">
                Topics
                <svg className="w-3 h-3 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              {/* Dropdown */}
              <div className="fixed left-0 right-0 top-24 opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out delay-150 z-50">
                <div className="bg-text-primary border-b border-background/20 shadow-2xl">
                  <div className="max-w-7xl mx-auto px-8 py-12">
                    <div className="space-y-1">
                      {TOPICS_LINKS.map((link) => (
                        <Link
                          key={link.href}
                          href={link.href}
                          className="block py-3 text-lg text-background hover:text-background/70 hover:pl-2 transition-all duration-300"
                        >
                          {link.label}
                        </Link>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Mobile menu button */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="md:hidden text-background absolute right-4"
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
          <div className="md:hidden py-4 space-y-3 border-t border-background/20">
            <Link href="/" className="block text-background hover:text-background/70 transition-colors font-medium">
              Home
            </Link>
            <Link href="/about" className="block text-background hover:text-background/70 transition-colors font-medium">
              About
            </Link>

            {/* Blog Accordion */}
            <div>
              <button
                onClick={() => toggleMobileDropdown('blog')}
                className="w-full flex items-center justify-between text-background hover:text-background/70 transition-colors font-medium"
              >
                Blog
                <svg className={`w-4 h-4 transition-transform duration-300 ${mobileDropdowns.blog ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div className={`overflow-hidden transition-all duration-500 ease-out ${mobileDropdowns.blog ? 'max-h-96 mt-2 opacity-100' : 'max-h-0 opacity-0'}`}>
                <div className="ml-4 space-y-2">
                  {BLOG_LINKS.map((link) => (
                    <Link key={link.href} href={link.href} className="block text-background/80 hover:text-background transition-colors text-sm">
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
                className="w-full flex items-center justify-between text-background hover:text-background/70 transition-colors font-medium"
              >
                Shop
                <svg className={`w-4 h-4 transition-transform duration-300 ${mobileDropdowns.shop ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div className={`overflow-hidden transition-all duration-500 ease-out ${mobileDropdowns.shop ? 'max-h-96 mt-2 opacity-100' : 'max-h-0 opacity-0'}`}>
                <div className="ml-4 space-y-2">
                  {SHOP_LINKS.map((link) => (
                    <Link key={link.href} href={link.href} className="block text-background/80 hover:text-background transition-colors text-sm">
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
                className="w-full flex items-center justify-between text-background hover:text-background/70 transition-colors font-medium"
              >
                Designs
                <svg className={`w-4 h-4 transition-transform duration-300 ${mobileDropdowns.designs ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div className={`overflow-hidden transition-all duration-500 ease-out ${mobileDropdowns.designs ? 'max-h-96 mt-2 opacity-100' : 'max-h-0 opacity-0'}`}>
                <div className="ml-4 space-y-2">
                  {DESIGNS_LINKS.map((link) => (
                    <Link key={link.href} href={link.href} className="block text-background/80 hover:text-background transition-colors text-sm">
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
                className="w-full flex items-center justify-between text-background hover:text-background/70 transition-colors font-medium"
              >
                Topics
                <svg className={`w-4 h-4 transition-transform duration-300 ${mobileDropdowns.topics ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div className={`overflow-hidden transition-all duration-500 ease-out ${mobileDropdowns.topics ? 'max-h-96 mt-2 opacity-100' : 'max-h-0 opacity-0'}`}>
                <div className="ml-4 space-y-2">
                  {TOPICS_LINKS.map((link) => (
                    <Link key={link.href} href={link.href} className="block text-background/80 hover:text-background transition-colors text-sm">
                      {link.label}
                    </Link>
                  ))}
                </div>
              </div>
            </div>

            <Link href="/work-with-us" className="block text-background hover:text-background/70 transition-colors font-medium">
              Work With Us
            </Link>
          </div>
        )}
      </nav>
    </header>
  );
}
