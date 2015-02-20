#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	FormatExternal
%include	/usr/lib/rpm/macros.perl
Summary:	HTML::FormatExternal - HTML to text formatting using external programs
Name:		perl-HTML-FormatExternal
Version:	22
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8db1ab6c3876d0633bbf22008459b42
URL:		http://search.cpan.org/dist/HTML-FormatExternal/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IPC-Run
BuildRequires:	perl-URI >= 0.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of formatter modules turning HTML into plain text
by dumping it through the respective external programs.

HTML::FormatText::Elinks HTML::FormatText::Html2text
HTML::FormatText::Links HTML::FormatText::Lynx
HTML::FormatText::Netrik HTML::FormatText::Vilistextum
HTML::FormatText::W3m HTML::FormatText::Zen

The module interfaces are compatible with HTML::Formatter modules such
as HTML::FormatText, but the external programs do all the work.

Common formatting options are used where possible, such as leftmargin
and rightmargin. So just by switching the class you can use a
different program (or the plain HTML::FormatText) according to
personal preference, or strengths and weaknesses, or what you've got.

There's nothing particularly difficult about piping through these
programs, but a unified interface hides details like how to set
margins and how to force input or output charsets.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/*.pm
%{perl_vendorlib}/HTML/FormatText
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
