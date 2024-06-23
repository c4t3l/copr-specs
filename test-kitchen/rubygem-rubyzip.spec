# Generated from rubyzip-2.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rubyzip

Name: rubygem-%{gem_name}
Version: 2.3.2
Release: 1%{?dist}
Summary: rubyzip is a ruby module for reading and writing zip files
License: BSD 2-Clause
URL: http://github.com/rubyzip/rubyzip
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.4
# BuildRequires: rubygem(coveralls) >= 0.7
# BuildRequires: rubygem(coveralls) < 1
# BuildRequires: rubygem(minitest) >= 5.4
# BuildRequires: rubygem(minitest) < 6
# BuildRequires: rubygem(pry) >= 0.10
# BuildRequires: rubygem(pry) < 1
# BuildRequires: rubygem(rubocop) >= 0.79
# BuildRequires: rubygem(rubocop) < 1
BuildArch: noarch

%description
rubyzip is a ruby module for reading and writing zip files.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/TODO
%{gem_libdir}
%{gem_instdir}/samples
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Mon Apr 03 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 2.3.2-1
- Initial package
